#@coding  :utf-8
#@FileName: sys 解释器交互.py
#@Author  :辰晨
#@Time    :2019/4/17 17:05

# python 解释器交互
# sys.argv           命令行参数List，第一个元素是程序本身路径
# sys.exit(n)        退出程序，正常退出时exit(0)
# sys.version        获取Python解释程序的版本信息
# sys.maxint         最大的Int值
# sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
# sys.platform       返回操作系统平台名称
# sys.stdout.write('please:')
# val = sys.stdin.readline()[:-1]
import sys

# print(sys.argv)
#
# if sys.argv[1] == 'post':
#     print(123)
#
# elif sys.argv[1] == 'download':
#     print(456)

# print(sys.path)
print(sys.platform)
import os
if sys.platform == 'win32':
    os.system('dir')