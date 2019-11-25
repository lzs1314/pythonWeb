#@coding  :utf-8
#@FileName: 随机数.py
#@Author  :辰晨
#@Time    :2019/4/17 15:24

import random

# print(random.random())  #0~1的随机数
# print(random.randint(1,8)) #1~8 包括8
# print(random.choice('hello'))
# print(random.choice(['123',4,[1,2]]))
# print(random.sample(['123',4,[1,2]],2))
# print(random.randrange(1,3)) #1~3 不包括3


# 验证码
def v_code():
    code = ''
    for i in range(5):
        if i == random.randint(0,4):
            add = random.randrange(10)
        else:
            add = chr(random.randrange(65, 91))
        code += str(add)
    print(code)

v_code()

def v_code1():
    code = ''
    for i in range(5):
        add = random.choice([random.randrange(10),chr(random.randrange(65, 91))])
        code += str(add)
    print(code)


v_code1()