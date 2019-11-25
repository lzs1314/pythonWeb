# @coding  :utf-8
# @FileName:12.py
# @Author  :
# @Time    :2019/11/20 12:55

import os
import random


songs_path = os.path.realpath(os.path.join(__file__, "../../static/mp3/"))
back_path = os.path.realpath(os.path.join(__file__, "../../static/mp3_back/"))

# 遍历songs目录, 获取所有歌曲文件名并区分歌曲名与歌手名
songs_list = os.listdir(songs_path)
name_or_singer = [song.replace(".mp3", '').split('-') for song in songs_list]

# 如果目录下存在有两个"-"的文件名则视为强制置顶排序歌曲(表白用的), 下面举个例子
# 李宗盛 - 我终于失去了你 - 1.mp3
# 陈奕迅 - 爱情转移 - 2.mp3
# 王力宏 - 你是我心内的一首歌 - 3.mp3
list1 = [name for name in name_or_singer if len(name) == 3]
list2 = [name for name in name_or_singer if len(name) < 3]

list1.sort(key=lambda x: int(x[2]))

rspid1 = [name[2].strip() for name in list1]
name1 = [name[1].strip() for name in list1]
singer1 = [name[0].strip() for name in list1]
songs1 = ["-".join(song) + ".mp3" for song in list1]

rspid2 = [i + len(rspid1) + 1 for i in range(len(list2))]
name2 = [name[1].strip() for name in list2]
singer2 = [name[0].strip() for name in list2]
songs2 = ["-".join(song) + ".mp3" for song in list2]

# 将置顶歌曲与其他歌曲合并
rspid = rspid1 + rspid2
name = name1 + name2
singer = singer1 + singer2
songs = songs1 + songs2

bgp_path = os.path.realpath(os.path.join(__file__, "../../static/image/"))
bgp_file = os.listdir(bgp_path)
bgp = []
for i in range(len(songs)):
    bgp.append(bgp_file[random.randint(0, len(bgp_file) - 1)])

resp_data = []
for i in range(len(rspid)):
    resp_data.append({
        "rspid": rspid[i],
        "songs": songs[i],
        "bgp": bgp[i],
        "name": name[i],
        "singer": singer[i]
    })
resp = {'status_code': 200, 'data': resp_data}
print(resp)
