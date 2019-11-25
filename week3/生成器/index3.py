#@coding  :utf-8
#@FileName: index3.py
#@Author  :辰晨
#@Time    :2019/4/17 16:00


#生成器

# 创建生成器两种方式
#     1.(x*2 for x in range(10))   >>>> generator object
#
#     2.def f():
#         yield 2
#         print()
#         f()  >>>>>> generator object
#
#     生成器的方法：
#         1.next(f())     >>>>>> 计算出一个值
#         注意：生成器在创建的时候已经决定了能计算出值的个数，调用
#         next的次数超过这个值就会报StopIteration
#
#         遍历所有元素可以通过for循环
#
#                 for i in [1,2,3]:
#                     print(i)
#
#             for  循环内部做了三件事
#                 1 调用对象的iter（）方法，返回一个迭代器对象
#                 2
#                     while:
#                         try:
#                             i = next(list_Iterator)
#                         except StopIteration:
#                             break
#             2 send()
#                 f().send() 等价于next(f())

# 迭代器
#
#
#     满足迭代器协议
#         1 内部有next()方法
#         2 内部有iter()方法

















