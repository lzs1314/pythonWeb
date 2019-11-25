# coding:utf-8
#@FileName: login.py
#@Author  :辰晨
#@Time    :2019/4/16 17:12


user,pwd = 'lzs',123

def login():
    user_name = input('user')
    password = input('pwd')
    if user_name == user and password == pwd:
        print('we')
    else:
        pass


@login
def home():
    print()



