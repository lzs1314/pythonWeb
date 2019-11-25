# coding:utf-8
# @FileName:列表生成器.py
# @Author  :辰晨
# @Time    :2019/4/17 10:56


def f(n):
    return n ** 3  # n的3次方


a = [x for x in range(10)]
print(a)

a = [x * 2 for x in range(10)]
print(a)

a = [f(x) for x in range(10)]
print(a)

