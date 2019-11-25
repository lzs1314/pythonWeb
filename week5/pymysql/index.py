# @coding  :utf-8
# @FileName:index.py
# @Author  :辰晨
# @Time    :2019/5/8 11:59


import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='student', charset='utf8')
# 创建游标
cursor = conn.cursor()

# inp = input('...')
# # 执行sql语句
# cursor.execute('insert into class(caption) values(%s)',inp)

# cursor.execute('insert into student(sname,class_id,gender) values(%s,%s,%s)',('请问',2,'男'))
# cursor.execute('update student set sname=%s where sid=%s',('请问',2))
# r = cursor.execute('select * from student where sid=2')
# cursor.execute('select name,pwd from user where name=%s and pwd=%s',('lzs','123'))
# r = cursor.fetchone()
# print(r)
cursor.execute('insert into class(caption) values(%s)', ('请'))
nid = cursor.lastrowid
print(nid)

# 查询所有
# result = cursor.fetchall()
# print(result)
# 查询第一条
# result = cursor.fetchone()
# print(result)
# 查询三条
# result = cursor.fetchmany(3)
# print(result)

conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()





