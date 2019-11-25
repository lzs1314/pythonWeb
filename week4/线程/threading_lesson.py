#@coding  :utf-8
#@FileName: threading_lesson.py
#@Author  :辰晨
#@Time    :2019/4/29 16:07


import threading
import time
# def foo(n):
#     pass
#
# t1 = threading.Thread(target=foo,args=(1,))
# t1.start()

class MyThread(threading.Thread):

    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):  #定义每个线程要运行的函数
        print('%s'%self.num)

        time.sleep(3)



if __name__ == '__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()

