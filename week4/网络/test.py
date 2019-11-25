#@coding  :utf-8
#@FileName: test.py
#@Author  :辰晨
#@Time    :2019/4/28 11:24


import subprocess

a = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE)
print(a)
