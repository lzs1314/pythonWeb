#@coding  :utf-8
#@FileName: post_clitet.py
#@Author  :辰晨
#@Time    :2019/4/28 15:29

import socket
import os

sk = socket.socket()
address = ('127.0.0.1',5000)
sk.connect(address)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
while True:
    inp = input('>>>').strip()

    cmd,path = inp.split('|')
    
    path = os.path.join(BASE_DIR,path)

    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size
    file_info = 'post|%s|%s'%(file_name,file_size)
    sk.sendall(bytes(file_info,'utf8'))


    f = open(path,'rb')

    has_send = 0
    while has_send != file_size:
        data = f.read(1024)
        sk.sendall(data)
        has_send+=len(data)

    f.close()
    print('success')

sk.close()



