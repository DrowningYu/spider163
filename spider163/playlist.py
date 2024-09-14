import utils
import requests
from bs4 import BeautifulSoup
import sys
import urllib.parse
import song
import json
import re
import time
def get_song_ids(playlist_id,father_folder_path,selenium_flag):
    url='https://music.163.com/playlist?id='+playlist_id
    html=requests.get(url,headers=utils.headers).content.decode()
    soup=BeautifulSoup(html,'lxml')
    playlist_name=soup.find(name='title').string.split(' - ')[0]
    soup_ur=soup.find(name='ul',attrs={'class':'f-hide'})
    lis=soup_ur.children
    ids=[]
    ids_str=""
    re_patter=r"id=(\d+)"
    for li in lis:
        link_dic=li.a.attrs
        match=re.search(re_patter,str(link_dic['href']))
        id=match.group(1)
        ids_str=ids_str+id+"/"
        ids.append(id)
    ids_str=ids_str[:-1]
    playlist_data={
        "ids":ids_str,
    }
    for id in ids:
        song_data=song.song_spider(id,father_folder_path,selenium_flag)
        playlist_data[id]=song_data
    return playlist_data

if __name__ == '__main__':
    playlist_id = sys.argv[1]
    # playlist_id = '8453578378'
    selenium_flag = sys.argv[2]
    # flag='false'
    father_folder_path = sys.argv[3]
    # father_folder_path='/d/Study/spider/spider163/spider163'

    data=get_song_ids(playlist_id,father_folder_path,selenium_flag)
    encoded_str = urllib.parse.quote(json.dumps(data))
    print(encoded_str)