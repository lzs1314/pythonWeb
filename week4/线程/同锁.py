#@coding  :utf-8
#@FileName: 同锁.py
#@Author  :辰晨
#@Time    :2019/4/29 16:27

import threading,time

def add():
    global num

    # num -=1
    r.acquire()
    temp = num
    time.sleep(0.001)
    num = temp-1
    r.release()


num = 100
thread = []

r = threading.Lock()
for i in range(100):
    t = threading.Thread(target=add)
    t.start()
    thread.append(t)

for t in thread:
    t.join()

print(num)



