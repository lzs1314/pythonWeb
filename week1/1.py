for i in range(1,10):
    for j in range(1,i+1):
        print('%d x %d = %d 	'%(j,i,i*j),end='')   #通过指定end参数的值，可以取消在末尾输出回车符，实现不换行。
    print()


import random
list1=[]
for i in range(65,91):
    list1.append(chr(i))        #通过for循环遍历asii追加到空列表中
for j in range (97,123):
    list1.append(chr(j))
for k in range(48,58):
    list1.append(chr(k))
ma = random.sample(list1,6)
print(ma)                      #获取到的为列表
ma = ''.join(ma)              #将列表转化为字符串
print(ma)



list1 = [2,3,8,4,9,5,6]
list2 = [5,6,10,17,11,2]
list3 = list1 + list2
print(list3)              #不去重只进行两个列表的组合
print(set(list3))         #去重，类型为set需要转换成list
print(list(set(list3)))



# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))

# 显示日历
print(calendar.month(yy, mm))



lis = [56,12,1,8,354,10,100,34,56,7,23,456,234,-58]
# 排序
def sortport():
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis
if __name__ == '__main__':
    sortport()
    print(lis)