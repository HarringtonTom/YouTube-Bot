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

Use for quick install: 
  
     sudo /home/user/YouTube-Bot/installer.sh

Install
------------
Download Repository:

    git clone https://github.com/HarringtonTom/YouTube-Bot.git YouTube-Bot

Make Scripts Executable: 

    chmod +x /home/user/YouTube-Bot/uploader.py
    chmod +x /home/user/YouTube-Bot/installer.sh
    chmod +x /home/user/YouTube-Bot/YouTube-Bot.sh

Make Folders for Videos: 

    mkdir /home/user/YouTube-Bot/videos
    mkdir /home/user/YouTube-Bot/archivedvideos
