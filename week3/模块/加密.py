#@coding  :utf-8
#@FileName: 加密.py
#@Author  :辰晨
#@Time    :2019/4/17 17:18


import hashlib

# m = hashlib.md5()
# print(m)
#
# m.update('hello'.encode('utf8'))
#
# print(m.hexdigest()) #5d41402abc4b2a76b9719d911017c592
#
# m.update('lzs'.encode('utf8'))
# print(m.hexdigest())


s = hashlib.sha256()
s.update('15169085700'.encode('utf8'))
print(s.hexdigest())


