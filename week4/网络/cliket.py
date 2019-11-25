#@coding  :utf-8
#@FileName: cliket.py
#@Author  :辰晨
#@Time    :2019/4/27 16:05

import socket

sk = socket.socket()

address = ('127.0.0.1',5000)

sk.connect(address)

while True:
    inp = input('输入')
    if inp == 'exit':break
    sk.send(bytes(inp,'utf8'))

    data = sk.recv(1024)

    print(str(data,'utf8'))

sk.close()

