import json
import sys
import urllib.parse
import bs4
import requests
import time
# from selenium import webdriver
from utils import headers_img
from utils import headers
from utils import creat_folder
from utils import trans_path
def get_url(id):
    url_pattern='https://music.163.com/song?id='
    return url_pattern+id

def load_song(path):
    path=path+'\\data.json'
    try:
        with open(path)as f:
            data=json.load(f)
        return data
    except FileNotFoundError:
        print('*json_file_can_not_find*')

def img_spider(url,path):
    format=url.split('/')[-1].split('.')[-1]
    path=path+'\\img.'+format
    res=requests.get(url,headers=headers_img)
    with open(path, 'wb') as file:
        file.write(res.content)
        file.close()
    return path
def lyric_spider(id):
    url='http://music.163.com/api/song/lyric?id='+id+'&lv=-1&kv=-1&tv=-1'
    data=json.loads(requests.get(url,headers=headers).content.decode())
    if(("tlyric" in data.keys())and("lrc" in data.keys())):
        return [data["tlyric"]["lyric"],data["lrc"]["lyric"]]
    else:
        return ["[00:00.00]纯音乐","[00:00.00]纯音乐"]
def music_data_spider(id,path):
    # path=path+'\\'+id+'.mp3'
    # path=trans_path(path)
    # url='music.163.com/song/media/outer/url?id='+id
    # res=requests.get(url,headers=headers).content
    # print(res.decode())
    # with open(path,'wb')as f:
    #     f.write(res)
    #     f.close()
    # return path
    return ""
def save_data(data,path):
    path=path+'\\data.json'
    path=trans_path(path)
    with open(path,'w') as f:
        json.dump(data,f,indent=4)
        f.close()
def song_spider(id,father_folder_path,selenium_flag):
    this_folder_path = father_folder_path + '/' + id
    [flag,music_path]=creat_folder(this_folder_path)
    if flag==1:#之前爬过该数据 就不爬了 直接加载之前的数据
        data=load_song(music_path)
        return data
    time.sleep(1)
    home_url=get_url(id)
    response=requests.get(home_url,headers=headers)
    de_res=response.content.decode()#访问
    soup=bs4.BeautifulSoup(de_res,'lxml')#解析

    title=soup.find(name='title')#爬title
    titles=title.string.split(' - ')
    music_name=titles[0]
    artists=titles[1]
    if(selenium_flag=="true"):
        music_data_path=music_data_spider(id,music_path)
    else:
        music_data_path=""
    music_img_url=soup.find(name='img',attrs={'class':'j-img'}).attrs['data-src']#爬封面
    music_img_path=img_spider(music_img_url,music_path)#存封面

    [lyric,lrc]=lyric_spider(id)#爬歌词

    data={
        "name":music_name,
        "artists":artists,
        "music_img":music_img_path,
        "music_data":music_data_path,
        "lyric":lyric,
        "lrc":lrc
    }
    save_data(data,this_folder_path)
    return data

if __name__ == '__main__':
    id = sys.argv[1]
    # id = '1853850798'
    #
    selenium_flag = sys.argv[2]
    # selenium_flag='true'
    #
    father_folder_path=sys.argv[3]
    # father_folder_path='/d/Study/spider/spider163/spider163'
    # father_folder_path = '/c/Users/DrowningYu/Desktop/AE/spider/spider163'


    data=json.dumps(song_spider(id,father_folder_path,selenium_flag))#json标砖格式转字符串
    encoded_str=urllib.parse.quote(data)

    print(encoded_str)
