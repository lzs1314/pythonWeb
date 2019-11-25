#@coding  :utf-8
#@FileName: post_server.py
#@Author  :辰晨
#@Time    :2019/4/28 15:29


import socket
import os

sk = socket.socket()
print(sk)
address=('127.0.0.1',5000)
sk.bind(address)
sk.listen(3)
print('------------------------------------')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print(BASE_DIR)
while 1:
    conn,addr = sk.accept()
    print(addr)
    while True:
        data = conn.recv(1024)
        cmd,file_name,file_size = str(data,'utf8').split('|')
        path = os.path.join(BASE_DIR,'yuan',file_name)
        file_size = int(file_size)

        f = open(path,'ab')
        has_receive = 0
        while 1:
            data = conn.recv(1024)
            f.write(data)
            has_receive+=len(data)

        f.close()




sk.close()


