
import httplib2
import os
import sys
import shutil
import time
import random
import subprocess

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

from parse_config import *

httplib2.RETRIES = 1
MAX_RETRIES = 10

SCOPE = "https://www.googleapis.com/auth/youtube.upload"

def get_refresh_token():
    try:
        flow = flow_from_clientsecrets(SECRET_PATH, SCOPE)
        storage = Storage(REFRESH_TOKEN_PATH)
        credentials = storage.get()

        if not credentials or credentials.invalid:
            credentials = run_flow(flow, storage)

        return True
    except:
        return False

if not REFRESH_TOKEN_EXISTS:
    get_refresh_token()
    REFRESH_TOKEN_EXISTS = True

def authorize_token():
    storage = Storage(REFRESH_TOKEN_PATH)
    credentials = storage.get()
    http = credentials.authorize(httplib2.Http())
    credentials.refresh(http)
    return build(API_NAME, API_VER, credentials=credentials)

def get_params(jsn):
    with open(os.path.join(VIDEOS_PATH, jsn)) as f:
        data = json.load(f)
        if not 'privacy' in data:
            data['privacy'] = DEFAULT_PARAMS['privacy']
        if not 'description' in data:
            if not 'description_file' in data:
                data['description'] = DEFAULT_PARAMS['description']
            else:
                try:
                    with open(data['description_file'], 'r') as f:
                        data['description'] = f.read()
                except:
                    data['description'] = DEFAULT_PARAMS['description']
        if not 'tags' in data:
            data['tags'] = DEFAULT_PARAMS['tags']
        if not 'title' in data:
            data['title'] = jsn.replace('.json', '', -1).title()
        if not 'categoryID' in data:
            data['categoryID'] = DEFAULT_PARAMS['categoryID']

    return data

def upload_all(pairs, default):
    if not default and not pairs:
        exit('No videos to upload.')
    if default:
        upload_default(default)
    if pairs:
        upload_paired(pairs)

def upload_paired(pairs):
    for video, jsn in pairs:
        params = get_params(jsn)
        uploaded = upload_vid(video, params)
        if uploaded:
            print(f"Uploaded {video}")
        if uploaded and DO_ARCHIVE_VIDEOS:
            archive_vid(video, jsn)
        

def upload_default(vids):
    params = DEFAULT_PARAMS.copy()
    for video in vids:
        params['title'] = video[:video.rindex('.')]
        uploaded = upload_vid(video, params)
        if uploaded:
            print(f"Uploaded {video}")
        if uploaded and DO_ARCHIVE_VIDEOS:
            archive_vid(video)

def upload_vid(video, parameters):

    def get_request():
        body = dict(
            snippet=dict(
                title=parameters['title'],
                description=parameters['description'],
                tags=parameters['tags'],
                categoryId=parameters['categoryID']
            ), status=dict(privacyStatus=parameters['privacy'])
        )

        return SERVICE.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=MediaFileUpload(os.path.join(VIDEOS_PATH, video), chunksize=-1, resumable=True)
        )

    request = get_request()

    uploaded = False
    status = None
    response = None
    error = None
    attempt = 0

    while response is None:

        try:

            status, response = request.next_chunk()
            if response is not None:
                if not 'id' in response:
                    break
                uploaded = True

        except HttpError as err:

            if err.resp.status in [500, 502, 503, 504]:
                attempt += 1
                if attempt >= MAX_RETRIES:
                    break

                max_sleep = 2 ** attempt
                sleep_seconds = random.random() * max_sleep
                time.sleep(sleep_seconds)

            elif err.resp.status == 400:
                print(f'Invalid parameters for {video}.')
                break
            else:
                exit('Daily limit reached. Try tommorow.')

        except Exception as e:
            attempt += 1
            if attempt >= MAX_RETRIES:
                break
    
            max_sleep = 2 ** attempt
            sleep_seconds = random.random() * max_sleep
            time.sleep(sleep_seconds)

    return uploaded


def archive_vid(video, jsn=None):
    old_vid_path = os.path.join(VIDEOS_PATH, video)
    new_vid_path = os.path.join(ARCHIVED_VIDEOS_PATH, video)
    shutil.move(old_vid_path, new_vid_path)

    if jsn is not None:
        old_jsn_path = os.path.join(VIDEOS_PATH, jsn)
        new_jsn_path = os.path.join(ARCHIVED_VIDEOS_PATH, jsn)
        shutil.move(old_jsn_path, new_jsn_path)


def main():
    global SERVICE

    video_file_list = [file for file in os.listdir(VIDEOS_PATH) if not file.endswith('.json')]
    video_jsons = [file for file in os.listdir(VIDEOS_PATH) if file.endswith('.json')]

    try:
        SERVICE = authorize_token()
        print('Token authorized.')
    except:
        exit("Couldn't authorize the token.")

    paired = []
    default_vids = []

    for video_f in video_file_list:
        if video_f.endswith('.txt'):
            continue
        try:
            dot = video_f.rindex('.')
            name = video_f[:dot]
            found_json = False
            for jsn in video_jsons:
                if jsn.replace('.json', '', -1) == name:
                    found_json = True
                    paired.append([video_f, jsn])
                    break
            if not found_json:
                default_vids.append(video_f)
        except:
            exit('Unsupported file type.')

    upload_all(pairs=paired, default=default_vids)

if __name__ == '__main__':
    main()
