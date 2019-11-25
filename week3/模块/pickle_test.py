#@coding  :utf-8
#@FileName: pickle_test.py
#@Author  :辰晨
#@Time    :2019/4/25 17:00

import pickle

dis = {'name':'lzs'}

data = pickle.dumps(dis)
f = open('pickle.test','w')

f.write(data)
f.close()
#
# f = open('json.test','rb')
#
# data = f.read()
# data = pickle.loads(data)
# print(data['name'])

