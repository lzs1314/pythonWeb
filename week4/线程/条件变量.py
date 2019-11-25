#@coding  :utf-8
#@FileName: 条件变量.py
#@Author  :辰晨
#@Time    :2019/5/5 11:29

import queue

d = queue.Queue(3)

d.put('qwe',0)
d.put('asd')
d.put('zxc')


print(d.get())
print(d.get())
print(d.get())
print(d.get())

