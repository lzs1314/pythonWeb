#@coding  :utf-8
#@FileName: cmd_cliket.py
#@Author  :辰晨
#@Time    :2019/4/28 11:16

import socket

sk = socket.socket()

address = ('127.0.0.1',5000)

sk.connect(address)

while True:
    inp = input('输入')
    if inp == 'exit':break
    sk.send(bytes(inp,'utf8'))
    result_len = int(str(sk.recv(1024),'utf8'))
    sk.sendall('ok')
    print(result_len)
    data = bytes()
    while len(data) != result_len:
        recv = sk.recv(1024)
        data+=recv
    # print(data)
    # data = sk.recv(1024)
    # while not data:
    #     data += sk.recv(1024)
    print(str(data,'gbk'))

sk.close()

