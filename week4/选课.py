#@coding  :utf-8
#@FileName: 选课.py
#@Author  :辰晨
#@Time    :2019/5/5 11:52

# import pickle
# #
# # class School:
# #
# #     def __init__(self,name):
# #         self.name = name
# #
# #     def save(self):
# #         pickle.dump((open('era.text'),'wb'),self)
# #
# #     @staticmethod
# #     def get_all():
# #         obj_list = []
# #
# #
# # s1 = School('shanghai')
# # s1.save()



arr = [1,2,3,4,5,6]
new=[]
old = []
# def main():
while len(arr) >0:
    arr1 = arr.pop()
    if (arr1%2==0):
        new.append(arr1)
    else:
        old.append(arr1)


print(new)
print(old)
# if __name__ == '__main__':
#     main()