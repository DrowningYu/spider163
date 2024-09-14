import utils
import requests
from bs4 import BeautifulSoup
import sys
import urllib.parse
import song
import json
import re
import time

# 先确保数据库连接上了再解了注释！不然会报错
# from dao import save_in_database

from utils import headers_img
def img_spider(url,path):
    format=url.split('/')[-1].split('.')[-1]
    path=path+'\\img.'+format
    res=requests.get(url,headers=headers_img)
    with open(path, 'wb') as file:
        file.write(res.content)
        file.close()
    return path
def get_song_ids(album_id,father_folder_path,db_flag):
    url='https://music.163.com/album?id='+album_id
    html=requests.get(url,headers=utils.headers).content.decode()
    soup=BeautifulSoup(html,'lxml')
    titles=soup.find(name='title').string.split(' - ')
    album_name=titles[0]
    asinger=titles[1]
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
    album_data={
        "aid":album_id,
        "aname":album_name,
        "asinger":asinger,
        "ids":ids_str,
    }
    for id in ids:
        song_data=song.song_spider(id,father_folder_path,db_flag)
        album_data[id]=song_data

    # 先确保数据库连接上了再解了注释！不然会报错
    # if(db_flag=="true"):
    #     result=save_in_database(album_data)
    #     if(result==0):
    #         print("done")
    #     elif(result==1):
    #         print("已存在")
    #     elif(result==2):
    #         print("失败")
    return album_data

if __name__ == '__main__':
    album_id = sys.argv[1]
    # album_id = '34897575'
    db_flag = sys.argv[2]
    # db_flag='false'
    father_folder_path = sys.argv[3]
    # father_folder_path='/d/AE_Project/spider163'


    # print(get_song_ids(album_id,father_folder_path,db_flag))
    data=get_song_ids(album_id,father_folder_path,db_flag)
    encoded_str = urllib.parse.quote(json.dumps(data))
    print(encoded_str)