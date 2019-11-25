# coding:utf-8
#@FileName: index1.py
#@Author  :辰晨
#@Time    :2019/4/17 11:55

#
# def bar():
#     print(8)
#     count = yield 1
#     print(count)
#     print(9)
#     yield 2
#
# b=bar()
# next(b)
# b.send('2')


# yield 伪并发

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("[%s]号包子来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)
        c2.send(i)

producer("alex")

# 通过生成器实现协程并行运算

# 生成器都是迭代器 ，迭代器不一定是生成器

l = [1,2,3,4]
l.__iter__()


# 什么是迭代器
#满足两个条件  1.有iter方法 2.有next方法











