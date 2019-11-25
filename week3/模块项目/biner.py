#@coding  :utf-8
#@FileName: bin.py
#@Author  :辰晨
#@Time    :2019/4/25 15:01

import sys
# import calculate
#
# print(calculate.add(1,3))
print(sys.path)  #搜索路径


# from calculate import add
# from calculate import *
from calculate import add as plus
print(add(1,3))
print(plus(1,3))