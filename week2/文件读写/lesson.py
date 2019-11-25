# coding:utf-8
# @FileName: lesson.py
# @Author  :辰晨
# @Time    :2019/4/13 15:41

import time  # 延迟时间

# r 读 read    w 写 write  清空以前数据  a 写 不清空以前的

f = open('小城市', 'a', encoding='utf8')
data = f.write('\n12 \n')
# f.write('123')

time.sleep(20)
print(data)

f.truncate()  # 截取从光标开始的位置到截取位置保留，其他删除
f.close()
