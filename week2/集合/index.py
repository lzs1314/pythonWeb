# coding:utf-8
#@FileName: index.py
#@Author  :辰晨
#@Time    :2019/4/15 16:25


import time


def f(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('日志','a') as f:
        f.write('%s action%s\n'%(time_current,n))

f(1)

