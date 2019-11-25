#@coding  :utf-8
#@FileName: shelve.py
#@Author  :辰晨
#@Time    :2019/4/25 17:12

import shelve

# f = shelve.open('shelve_test')
#
# f['info'] = {'name':'lzs'}


f = shelve.open('shelve_test')
data = f.get('info')
print(data)

data = f.get('info','hp')