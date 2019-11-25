# coding:utf-8
#@FileName: index.py
#@Author  :辰晨
#@Time    :2019/4/17 11:02



s = (s*2 for s in range(10))

print(next(s))


for i in s:
    print(i)


def foo():
    print('ok')
    yield 1

g=foo()

print(g) #<generator object foo at 0x000001DD5860A390>
next(g)

for i in foo():
    print(i)

#什么是可迭代对象(对象拥有__iter__方法的)

def fib(max):
    n,before, after = 0,0,1
    while n<max:
        # print(after)
        yield before
        before,after = after,before+after
        n=n+1

print(fib(8))