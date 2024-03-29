#__author:  Administrator
#date:  2016/10/26

def sqlexec(last_nid, is_next):
    import pymysql

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='IndexDB', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行存储过程,获取存储过程的结果集，将返回值设置给了  @_存储过程名_序号 =
    if is_next:
        cursor.execute('select * from tb1 where nid>%s limit 10',last_nid)
        result = cursor.fetchall()
    else:
        cursor.execute('select * from tb1 where nid<%s order by nid desc limit 10', last_nid)
        result = cursor.fetchall()
        result = list(reversed(result))

    conn.commit()
    cursor.close()
    conn.close()
    return result

current_last_nid = 0
current__nid = 0
while True:
    p = input('1、上一页; 2、下一页\n')
    if p == '2':
        # 点击下一页
        is_next = True
        ret = sqlexec(current_last_nid, is_next)
    else:
        is_next = False
        ret = sqlexec(current_first_nid, is_next)
    current_first_nid = ret[0]['nid']
    current_last_nid = ret[-1]['nid']
    for i in ret:
        print(i)