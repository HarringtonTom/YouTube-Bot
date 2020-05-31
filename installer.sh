#!/bin/bash

echo "Updating Packages..." 
sudo apt update > /dev/null 2>&1
sudo apt upgrade -y > /dev/null 2>&1

echo "Installing Python..."
sudo apt install -y python3 > /dev/null 2>&1
sudo apt install -y python3-pip > /dev/null 2>&1 
pip3 install -y google-api-python-client > /dev/null 2>&1
pip3 install -y google-auth-oauthlib > /dev/null 2>&1
pip3 install -y google-auth-httplib2 > /dev/null 2>&1
pip3 install -y oauth2client > /dev/null 2>&1

echo "Installing YouTube-dl..."
sudo pip3 install -y youtube_dl > /dev/null 2>&1

echo "Installing ffmpeg..." 
sudo apt install -y ffmpeg > /dev/null 2>&1

echo -e "\e[31mInstallation Complete" 

echo -e "\e[39m" 

 
