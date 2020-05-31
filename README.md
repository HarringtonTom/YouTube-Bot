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

General
------------
- **videos** - Folder that Videos are downloaded to
- **archivedvideos** - Folder of Videos that have already been uploaded (Stops them from being reuploaded everytime script runs)
- **client_secret.json** - Used to log into Google Account 
- **refresh_token.json** - Used to log into YouTube Brand Account

Install
------------
**Download Repository:**

    git clone https://github.com/HarringtonTom/YouTube-Bot.git YouTube-Bot

**Make Scripts Executable:** 

    cd YouTube-Bot
    chmod +x ./installer.sh
    chmod +x ./run.py
    chmod +x ./YouTube-Bot.sh

**Install Packages:** 

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

**Make Folders for Videos:** 

    cd YouTube-bot
    mkdir videos
    mkdir archivedvideos

**Create 'client_secret.json'** 

- Go to Google API Console - https://console.developers.google.com/
- Create new Project and name as "YouTube Uploader" or anything you want :) 
- Go to API's and Services and enable the "YouTube Data API" 
- Go to OAuth consent screen and register. Set User Type to External, Enter Application Name and leave the rest default. 
- Go to Credentials and create new OAuth client ID credential. Choose any Application type doesn't really matter and name as YouTube Uploader again. 
- Now download the client secret json file to the YouTube-Bot Folder and make sure to rename to client_secret.json

**Setup 'config' File**

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

**Add Description and Channel/Playlist list:** 

    cd YouTube-Bot
    sudo nano channel_list.txt
    sudo nano description.txt
    
**Edit Script:** 

    cd YouTube-Bot
    sudo nano YouTube-Bot.sh

Add YouTube-dl Command

    youtube-dl --playlist-end 2 --download-archive '/home/user/YouTube-Bot/downloaded.txt' -i -o "/home/user/YouTube-Bot/videos/%(title)s" -f bestvideo+bestaudio --merge-output-format mkv --batch-file='/home/user/YouTube-Bot/channel_list.txt'
    
   **--playlist-end 2** = Only scans the last 2 videos in the playlist which speeds up scanning
   
   **--download-archive** = Links to all the videos you've downloaded so that YouTube-dl doesn't keep downloading them

Edit Python script location

    python3 '/home/user/YouTube-Bot/run.py'

**Setup YouTube Uploader:** 

    cd YouTube-Bot
    python3 run.py
 
 - Go to the link in Browser and use it to log into your YouTube Brand Account 
 - Give YouTube Uploader permission to your Account
 - Copy code and paste

**Test YouTube-Bot Script:** 

    cd YouTube-Bot
    ./YouTube-Bot.sh

 - The Script should now download and upload your chosen Videos

**Automate the Process:** 
   
    crontab -e
    
    * * * * * '/home/user/YouTube-Bot/YouTube-Bot.sh'

I also recommend adding a log file, so that if the Script doesn't work you can see why: 

    * * * * * '/home/user/YouTube-Bot/YouTube-Bot.sh' 1> /dev/null 2> /home/user/YouTube-Bot.err

**YOU ARE NOW DONE, I HOPE YOU ENJOY THE SCRIPT**
