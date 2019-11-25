# @coding  :utf-8
# @FileName: s1.py
# @Author  :辰晨
# @Time    :2019/4/27 15:12


# import s2
#
# inp = input('')
#
# if hasattr(s2,inp):
#     func = getattr(s2,inp)
#     result = func()
#     print(result)
# else:
#     print(404)


class Foo:
    __v = None

    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__ = Foo()
            return cls.__v


obj = Foo.get_instance()
print(obj)
