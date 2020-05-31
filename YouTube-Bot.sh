#!/bin/bash

#fixes the issue of YouTube-dl not being found in crontab
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
 
#enter your youtube-dl command here, look at example in README
youtube-dl --playlist-end 2 --reject-title 'Photos' --download-archive '/home/tjh/YouTube-Bot/downloaded.txt' -i -o "/home/tjh/YouTube-Bot/videos/%(title)s" -f bestvideo+bestaudio --merge-output-format mkv --batch-file='/home/tjh/YouTube-Bot/channel_list.txt' 

#change user to your user name
python3 '/home/tjh/YouTube-Bot/run.py'
