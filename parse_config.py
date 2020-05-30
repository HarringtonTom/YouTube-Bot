import json
import os

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_config():
    with open(os.path.join(CURRENT_DIR, 'config.json'), 'r') as f:
        config = json.load(f)
    return config

_config = get_config()

API_NAME = _config['API_name']
API_VER = _config['API_ver']

if os.path.isdir(_config['videos_path']):
    VIDEOS_PATH = _config['videos_path']
else:
    exit('Videos path doesn\'t exist.')

DO_ARCHIVE_VIDEOS = _config['do_archive_videos']

if DO_ARCHIVE_VIDEOS:
    if os.path.isdir(_config['archived_videos_path']):
        ARCHIVED_VIDEOS_PATH = _config['archived_videos_path']
    else:
        os.makedirs(ARCHIVED_VIDEOS_PATH)
    
if os.path.isfile(_config['secret_path']):
    SECRET_PATH = _config['secret_path']
else:
    exit('Secret path doesn\'t exist')

if _config['refresh_token_path'] == '':
    REFRESH_TOKEN_PATH = os.path.join(CURRENT_DIR, 'refresh_token.json')
else:
    REFRESH_TOKEN_PATH = _config['refresh_token_path']

REFRESH_TOKEN_EXISTS = os.path.isfile(REFRESH_TOKEN_PATH)
DEFAULT_PARAMS = _config["default_parameters"]
if DEFAULT_PARAMS['description_as_file']:
    with open(DEFAULT_PARAMS['description'], 'r') as f:
        DEFAULT_PARAMS['description'] = f.read()

del _config
del get_config