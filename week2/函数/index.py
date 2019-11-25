# coding:utf-8
# @FileName: index.py
# @Author  :辰晨
# @Time    :2019/4/16 10:45


# def add(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
#
# add(1, 2, 3, 4, 5)


def print_info(*args, **kwargs):
    print(args)
    print(kwargs)


print_info(12, 'lzs', qwe='qwe')


# 递归
def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


print(fact(5))


def fat(n):
    red = 1
    for i in range(1, n + 1):
        red = i * red
    return red


print(fat(5))

import time


# def show_time(func):   #传入函数名
#     start = time.time()
#     func()
#     end = time.time()
#     print('%s'%(end-start))
#
# show_time(f)

# 高级版  装饰器
def show_time(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        print('%s' % (end - start))

    return inner


# show_time(f)()
@show_time  # 相当于 f = show_time(f)
def f():
    print('foo')
    time.sleep(1)


f()


def logger(flag):
    def show_time(f):
        def inner(*x, **y):
            start = time.time()
            f(*x, **y)
            end = time.time()
            print('%s' % (end - start))

        return inner

    return show_time


@logger('we')
def add(*a, **b):
    sun = 0
    for i in a:
        sun += i
    print(sun)
    time.sleep(1)


add(1, 2, 3, 4, 5)
