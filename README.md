# YouTube-Bot
A bot that downloads from chosen YouTube Channels/Playlists and then re-uploads on your own Channel. 

Requirements
------------
- sudo apt install git
- sudo apt install python3
- sudo apt install python3-pip
- sudo pip3 install youtube_dl
- sudo apt install ffmpeg
- pip3 install google-api-python-client
- pip3 install google-auth-oauthlib 
- pip3 install google-auth-httplib2
- pip3 install oauth2client

Install
------------
Download Repository:

    git clone https://github.com/HarringtonTom/YouTube-Bot.git YouTube-Bot

Make Scripts Executable: 

    cd YouTube-Bot
    chmod +x ./installer.sh
    chmod +x ./upload.py
    chmod +x ./YouTube-Bot.sh

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

