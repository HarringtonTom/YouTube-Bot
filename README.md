# YouTube-Bot
A bot that downloads from chosen YouTube Channels/Playlists and then re-uploads on your own Channel. 

Requirements
------------
- python3
- python3-pip
- youtube_dl
- ffmpeg
- google-api-python-client
- google-auth-oauthlib 
- google-auth-httplib2
- oauth2client

Install
------------
Download Repository:

    git clone https://github.com/HarringtonTom/YouTube-Bot.git YouTube-Bot

Make Scripts Executable: 

    cd YouTube-Bot
    chmod +x ./installer.sh
    chmod +x ./upload.py
    chmod +x ./YouTube-Bot.sh

Install Packages: 

    cd YouTube-Bot
    sudo ./installer.sh

Or Install Manually: 
    
    sudo apt install python3
    sudo apt install python3-pip
    sudo pip3 install youtube_dl
    sudo apt install ffmpeg
    pip3 install google-api-python-client
    pip3 install google-auth-oauthlib 
    pip3 install google-auth-httplib2
    pip3 install oauth2client

Make Folders for Videos: 

    cd YouTube-bot
    mkdir videos
    mkdir archivedvideos

Create 'client_secret.json' 

- Go to Google API Console - https://console.developers.google.com/
- Create new Project and name as "YouTube Uploader" or anything you want :) 
- Go to API's and Services and enable the "YouTube Data API" 
- Go to OAuth consent screen and register. Set User Type to External, Enter Application Name and leave the rest default. 
- Go to Credentials and create new OAuth client ID credential. Choose any Application type doesn't really matter and name as YouTube Uploader again. 
- Now download the client secret json file to the YouTube-Bot Folder and make sure to rename to client_secret.json

Setup 'config' 

    cd YouTube-Bot
    sudo nano config.json

Edit it however you want, but make sure to change 'user'. 

    {
        "API_name": "youtube",
        "API_ver": "v3",
        "videos_path": "/home/user/YouTube-Bot/videos/",
        "archived_videos_path": "/home/user/YouTube-Bot/archivedvideos/",
        "do_archive_videos": true,
        "secret_path": "/home/user/YouTube-Bot/client_secret.json",
        "refresh_token_path": "",
        "default_parameters": {
            "privacy": "public",
            "description": "/home/user/YouTube-Bot/description.txt",
            "description_as_file": true,
            "tags": ["lol", "lmao"],
            "categoryID": 24
        }
    }

Add Description and Channel/Playlist list: 

    cd YouTube-Bot
    sudo nano channel_list.txt
    sudo nano description.txt
