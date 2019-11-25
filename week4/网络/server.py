#@coding  :utf-8
#@FileName: server.py
#@Author  :辰晨
#@Time    :2019/4/27 15:54

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
        print(str(data,'utf8'))
        if not data: break
        inp = input('输入')
        conn.send(bytes(inp,'utf8'))

sk.close()

# server
#     bind()
#     listen()
#     accept()
#
#     recv()
#     send(string)
#     sendall()

# cliket
#     recv()
#     send(string)
#     sendall()














