import os
headers={
    'Referer':'https://music.163.com/',
    'Host':'music.163.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
}
headers_img = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Tue, 15 Mar 2022 09:11:15 Asia/Shanghai',
    'If-None-Match': '675e915d924fca79e8cabb5f4365e2aa',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
def trans_path(path):
    path=path.replace('/','\\')
    path=path[1:]
    new_path=path[:1]+':'+path[1:]
    return new_path
def creat_folder(path):
    if '/' in path:
        path=trans_path(path)
    if not os.path.exists(path):
        os.makedirs(path)
        return[0,path]
    return [1,path]