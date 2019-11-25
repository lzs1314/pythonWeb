#@coding  :utf-8
#@FileName: index.py
#@Author  :辰晨
#@Time    :2019/4/27 9:12

# 面向对象
#     class  名字叫类
#     def    名字叫方法
#            方法得第一个参数是self

# 执行
#     中间人 = 类名()
#     中间人.方法

# self
#     self代指 调用方法得 对象（中间人）
# class Bar:
#     def foo(self,name):
#         print(name)
#
# ret = Bar()
# ret.foo('lzs')

# class Bar:
#     def foo(self,name):
#         print(self,name)
#
# ret = Bar()
# print(ret)
# ret.foo('lzs')


#
# class Bar:
#     # 构造方法
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def foo(self):
#         print(self.name,self.age)
#
# ret = Bar('lzs',18)
# print(ret)
# ret.foo()


#继承(F)
# class 父类：
#     pass
# class 子类（父类）：
    # pass

# 重写
#   防止执行父类中的方法

# self 永远是执行改方法的调用者

# super继承父类
#     super(子类,self).父类中的方法()
#     或者 父类名.父类方法(self)

# 支持多继承
#     左侧优先 一条走到黑
#     有公共基的时候走到基时候走另一边一直到基(同一个根，根最后执行)

# 面向对象三大特性之三：多态
class F:
    def f1(self):
        print('f1')

    def f2(self):
        print('f2')

class S(F):
    def s1(self):
        print('s1')

    def f2(self):
        F.f2(self)       #主动调用  执行父类（基类）中的方法
        # super(S,self).f2()  #执行父类（基类）中的方法
        print('sf2')


ret = S()
ret.s1()
ret.f2()

# 类成员
    # 字段
        # 静态字段属于类 保存在类  执行可以通过类或者对象访问
        # 普通字段属于对象，保存在对象 执行只能通过对象访问
    # 方法
        #普通方法 保存在类 有对象调用 self
        #静态方法 保存在类 有类直接调用
            # 类方法 保存在类 有类直接调用 cls
        # 如果对象中需要保存一些值 执行某功能时 需要使用对象中的值  普通方法
        # 不需要任何对象中的值 静态方法


class Foo:
    def bar(self):
        print(1)

    @staticmethod   #静态方法
    def start():
        print(2)

    @classmethod    #类方法
    def classmd(cls):  #cls 是类名
        print(3)

    @property      #属性 不伦不类
    def per(self):
        return 1

    @per.setter
    def per(self,va):
        print(va)


# 成员修饰符
#     共有成员
#     私有成员  __字段名（两个下划线）

# 特殊成员
#     __init__     类()自动执行
#     __call__     对象()  类()() 自动执行
#     __int__      int(对象)
#     __str__      str()
#     __dict__     讲对象中封装的所有的内容通过字典的形式返回
#     __getitem__  切片（slice）或者索引
#     __setitem__
#     __delitem__
#     __iter__

# metaclass 类的祖宗
#   python 中一切事物都是对象
#