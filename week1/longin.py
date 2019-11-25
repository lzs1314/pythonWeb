# coding:utf-8
#@FileName: longin.py
#@Author  :
#Time :2019/4/12 16:12


user_l = '1'
pwd_ws = '2'
# for i in range(3):
#     user = input('name')
#     pwd = input('pass')
#     flag = False
#     if user == user_l and pwd == pwd_ws:
#         flag = True
#         print('welcome %s login' %user_l)
#         break
#     else:
#         print('错误')
#
# if not flag:
#     print('明天再来')


# for i in range(3):
#     user = input('name')
#     pwd = input('pass')
#     if user == user_l and pwd == pwd_ws:
#         print('welcome %s login' %user_l)
#         break
#     else:
#         print('错误')
# else:
#     print('明天再来')

sec = 0
while sec <3:
    user = input('name')
    pwd = input('pass')
    if user == user_l and pwd == pwd_ws:
        print('welcome %s login' %user_l)
        break
    else:
        print('错误')
    sec += 1
else:
    print('明天再来')

# for i in range(1,101,2):
#     print(i)


