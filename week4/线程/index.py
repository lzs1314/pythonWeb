#@coding  :utf-8
#@FileName: index.py
#@Author  :辰晨
#@Time    :2019/4/29 11:30

from time import ctime,sleep
import threading

# start = time.time()
#
# def foo(n):
#     print('foo%s'%n)
#     time.sleep(1)
#
# def bar(n):
#     print('bar%s' % n)
#     time.sleep(2)
# # foo()
# # bar()
# t1 = threading.Thread(target=foo,args=(1,))
# t2 = threading.Thread(target=bar,args=(2,))
# t1.start()
# t2.start()
#
# print('----------------------')
#
# t1.join()
# t2.join()
#
# print('----------------------')
# end = time.time()
# print(end - start)

# start = time.time()
# def add(n):
#     sun = 0
#     for i in range(n):
#         sun+=i
#     print(sun)
#
# # add(10000000)
# # add(20000000)
#
#
#
# t1 = threading.Thread(target=add,args=(10000000,))
# t1.start()
#
# t2 = threading.Thread(target=add,args=(20000000,))
# t2.start()
#
# t1.join()
# t2.join()
#
#
# end = time.time()
# print(end - start)


def music(func):
    for i in range(2):
        print('music start %s. %s '%(func,ctime()))
        sleep(3)
        print('music end %s' %ctime())

def move(func):
    for i in range(2):
        print('move start %s! %s '%(func,ctime()))
        sleep(5)
        print('move end %s'%ctime())

threads = []

t1 = threading.Thread(target=music,args=('七里香',))
threads.append(t1)

t2 = threading.Thread(target=move,args=('阿甘',))
threads.append(t2)

if __name__ == '__main__':
    t2.setDaemon(True)
    for t in threads:
        t.start()
        # t.join()

    print('all %s'%ctime())



















