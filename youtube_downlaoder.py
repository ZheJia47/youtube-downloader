# 在python資料夾底下執行“Install Certificates.command”解決驗證問題
# cd "/Applications/Python 3.8/" 
# sudo "./Install Certificates.command"

from pytube import YouTube
import os
from pprint import pprint

while True:
    download_link = input('輸入下載網址: ')
    yt = YouTube(download_link)

    # save path
    save_path = os.path.expanduser('~') + '/Downloads/music' 

    pprint(yt.streams.all())
    index = int(input('index = '))
    yt.streams.all()[index].download(save_path)

    if download_link == 'q': break


# todo: youget    

