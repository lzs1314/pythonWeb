#@coding  :utf-8
#@FileName: json_test.py
#@Author  :辰晨
#@Time    :2019/4/25 16:53

import json

# dis = {'name':'lzs'}
#
# data = json.dumps(dis)
# f = open('json.test','w')
#
# f.write(data)
# f.close()

# f = open('json.test','r')
#
# data = f.read()
# data = json.loads(data)
# print(data['name'])



dis = {'name':'lzs'}


# f = open('json.test','w')
# json.dump(dis,f)
# f.close()


f = open('json.test','r')
data = json.load(f)
print(data['name'])