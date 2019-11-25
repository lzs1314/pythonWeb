# print(input("请输入姓名："))

# 感觉要出错用try
def student(s,y):
    try:
        a = s+ y
        print(a)
    # except Exception as e: #错误信息
    #     print(e)

    except:
        print(1)

student('1',4)