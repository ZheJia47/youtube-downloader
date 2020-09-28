# 在python資料夾底下執行“Install Certificates.command”解決驗證問題
# cd "/Applications/Python 3.8/" 
# sudo "./Install Certificates.command"

from pytube import YouTube
import os
from pprint import pprint
from selenium import webdriver
from time import sleep

# browser=webdriver.Chrome()
# path to save file
save_path = os.path.expanduser('~') + '/Downloads/music' 

while True:
    download_link = input('輸入下載網址: ')

    # todo: use 'youtube + to' website to download
    # browser.get(download_link)



    # use pytube ######################
    yt = YouTube(download_link)
    pprint(yt.streams.all())
    index = int(input('index = '))
    yt.streams.all()[index].download(save_path)

    if download_link == 'q': break

