def demo(b):
    print('as', b)
    a = 88
    return a


a = demo(99)
print(a)


# 有一个外部函数，有一个内部函数，内部函数用到外部函数的变量，外部函数返回内部函数的引用
# 函数的引用
# def demo_1(name):
#     a = 88
#     def demo_2():
#         print(a,name)
#     return  demo_2
# num = demo_1('lzs')
# num()
def demo_1(name):
    a = 88

    def demo_2():
        print(a)

    return demo_2


@demo_1
def test_1():
    print('这是一段功能函数')


test_1()

name = input('qwe')
age = input('qwe')

# ''' 打印多行 '''
# %s   s = string    占位符
# %d   d = digit 整数
# %f   f = float 浮点数，约等于小数

msg = '''            
name: %s
age : %s
''' % (name, age)
print(msg)
