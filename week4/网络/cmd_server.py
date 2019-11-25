#@coding  :utf-8
#@FileName: cmd_server.py
#@Author  :辰晨
#@Time    :2019/4/28 11:16


import subprocess

import socket

# family type

sk = socket.socket()
print(sk)
address=('127.0.0.1',5000)
sk.bind(address)
sk.listen(3)
print('------------------------------------')

while 1:
    conn,addr = sk.accept()
    print(addr)
    while True:
        try:
            data = conn.recv(1024)
        except Exception as e:
            print(e)
            break
        if not data: break
        print(str(data, 'utf8'))

        obj = subprocess.Popen(str(data,'utf8'),shell=True,stdout=subprocess.PIPE)
        cmd_result = obj.stdout.read()
        result_len = bytes(str(len(cmd_result)),'utf8')
        conn.sendall(result_len) #粘包现象
        conn.recv(1024)
        conn.sendall(cmd_result)
        #两个sendall 一起可能出现粘包现象 解决办法加个阻塞
sk.close()
