#@coding  :utf-8
#@FileName: 时间.py
#@Author  :辰晨
#@Time    :2019/4/17 14:31

import time

# print(help(time))

# print(time.time()) #1555483039.2118325 时间戳
# print(time.asctime()) # 时间
# time.sleep(3)
# print(time.perf_counter()) # 计算cpu执行时间
# print(time.ctime()) # 时间

# print(time.gmtime()) # 结构化时间
# print(time.localtime()) #本地时间
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) #字符串时间日期
# a = time.strptime('2019-04-17 15:06:26','%Y-%m-%d %H:%M:%S')
# print(a.tm_hour)
# print(a.tm_wday)
# print(time.mktime(time.gmtime())) #转化时间戳

# 时间戳，结构化时间，格式化时间

# print(time.ctime(1555485395.0))



import datetime

print(datetime.datetime.now())


