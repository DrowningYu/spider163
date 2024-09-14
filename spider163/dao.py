import pymysql
from datetime import date
db=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    database="musicdb",
)
def save_in_database(data):
    cursor=db.cursor()
    try:
        result=cursor.execute("SELECT * FROM album WHERE aid='%s'"%(data["aid"]))
        if(result!=0):
            return 1#已存在
        current_date = date.today()
        formatted_date = current_date.strftime('%Y-%m-%d')
        cursor.execute("INSERT INTO album VALUES (%d, '%s', '%s', '', '%s')" % (int(data["aid"]), data["aname"], data["asinger"], formatted_date))
        db.commit()

        ids=data['ids'].split("/")
        for id in ids:
            song_data=data[id]
            song_data['lyric'] = song_data['lyric'].replace("'", "/single_quote/")
            song_data['lrc'] = song_data['lrc'].replace("'", "/single_quote/")

            cursor.execute("INSERT INTO song VALUES (%d,%d,'%s','%s','%s',0,'%s')"
                           %(int(id), int(data['aid']), song_data['name'], song_data['artists'], song_data['lyric'], song_data['lrc']))#oid aid sname singer lyric stype lrc
            db.commit()
    except:
        return 2
    db_data = cursor.fetchall()
    cursor.close()
    db.close()
if __name__ == '__main__':
    data={"aid":"233",
        "aname":"test",
        "asinger":"me",
        "ids":"123/234",
          "123":{
              "name": "test_1",
              "artists": "noshrimp",
              "music_img": "",
              "music_data": "",
              "lyric": "纯音乐",
              "lrc": "纯音乐"
          },
          "234":{
              "name": "test_1",
              "artists": "mlkong",
              "music_img": "",
              "music_data": "",
              # "lyric": "纯音乐",

              "lyric": "[00:00.00] 作词 : Andrew Taggart/Nirob Islam/SHY Martin\n[00:01.00] 作曲 : Andrew Taggart/Nirob Islam/Sara Hejellstrom\n[00:10.80]Fighting flames of fire\n[00:13.38]Hang onto burning wires\n[00:16.02]We don't care anymore\n[00:21.40]Are we fading lovers?\n[00:23.92]We keep wasting colors\n[00:26.66]Maybe we should let this go\n[00:29.92]\n[00:31.57]We're falling apart, still we hold together\n[00:36.89]We've passed the end so we chase forever\n[00:41.89]Cause this is all we know\n[00:47.36]This feeling's all we know\n[00:51.60]\n[00:52.00]I'll ride my bike up to the road\n[00:55.02]Down the streets right through the city\n[00:57.71]I'll go everywhere you go\n[01:00.26]From Chicago to the coast\n[01:02.96]You tell me, \"Hit this and let's go\n[01:05.68]Blow the smoke right through the window\"\n[01:08.72]Cause this is all we know\n[01:21.90]Cause this is all we know\n[01:32.72]Cause this is all we know\n[01:35.75]\n[01:36.12]Never face each other\n[01:38.62]one bed, different covers\n[01:41.31]We don't care anymore\n[01:46.64]Two hearts still beating\n[01:49.26]On with different rhythms\n[01:51.96]Maybe we should let this go\n[01:54.80]\n[01:56.76]We're falling apart, still we hold together\n[02:01.96]We've passed the end so we chase forever\n[02:07.28]Cause this is all we know\n[02:12.65]This feeling's all we know\n[02:17.02]\n[02:17.35]I'll ride my bike up to the road\n[02:20.31]Down the streets right through the city\n[02:22.93]I'll go everywhere you go\n[02:25.62]From Chicago to the coast\n[02:28.06]You tell me, \"Hit this and let's go\n[02:30.95]Blow the smoke right through the window\"\n[02:33.98]Cause this is all we know\n[02:47.37]Cause this is all we know\n[02:57.92]Cause this is all we know\n",
              # "lrc": "123"
              "lrc":"[by:咆哮的小清新___]\n[00:10.80]宛若在烈焰中苦苦挣扎\n[00:13.38]倔强将火中之栗在手中紧握\n[00:16.02]不在意伤痕痛苦的你我\n[00:21.40]我们是否已经走到尽头\n[00:23.92]再多挣扎也只是徒增苦愁\n[00:26.66]也许是时候该放手\n[00:31.57]渐行渐远的你我 依然将双手紧握\n[00:36.89]相信挺过这难关 爱或许就能永久\n[00:41.89]这就是我们为何而坚守\n[00:47.36]这就是我们共同拥有的感受\n[00:52.00]骑着单车的我 欲将这世界环游\n[00:55.02]横穿这城市 在转角的街头直走\n[00:57.71]无论你到哪 我都跟着你走\n[01:00.26]哪怕是从芝加哥到西海岸的尽头\n[01:02.96]想起你对我说过 决定了就即刻行动\n[01:05.68]想起在车窗前吞云吐雾那般自在的时候\n[01:08.72]这就是我们共同的拥有\n[01:21.90]这也是我们都记得的感受\n[01:32.72]我们都记得 都认同 都共同拥有\n[01:36.12]不再见面的你我\n[01:38.62]心还连着 但眼前风景却早已不同\n[01:41.31]也不能再像从前那般关怀问候\n[01:46.64]两颗心依旧为彼此跳动\n[01:49.26]却渐渐不再是相同的频率和节奏\n[01:51.96]也许真的是时候该放手\n[01:56.76]渐行渐远的你我 依然在为彼此坚守\n[02:01.96]相信挺过这难关 爱或许就能永久\n[02:07.28]这就是我们为何而坚守\n[02:12.65]这就是我们共同拥有的感受\n[02:17.35]骑着单车的我 欲将这世界环游\n[02:20.31]横穿这城市 在转角的街头直走\n[02:22.93]无论你到哪 我都跟着你走\n[02:25.62]哪怕是从芝加哥到西海岸的尽头\n[02:28.06]想起你对我说过 决定了就即刻行动\n[02:30.95]想起在车窗前吞云吐雾那般自在的时候\n[02:33.98]这就是我们共同的拥有\n[02:47.37]这也是我们都记得的感受\n[02:57.92]我们都记得 都认同 都共同拥有\n"
          }
          }
    save_in_database(data)