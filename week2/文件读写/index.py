# coding:utf-8
# @FileName: index.py
# @Author  :辰晨
# @Time    :2019/4/15 9:20

import sys, time

# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(0.2)

for i in range(30):
    print('*', end='', flush=True)
    time.sleep(0.2)
