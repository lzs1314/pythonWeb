
# 学生信息列表数组
#
# 1。查询所有的学生信息
# 2。搜索学生信息
# 3。增加学生信息
# 4。修改学生信息
# 5。删除学生信息
# 6。退出系统
#

student_list =[]

def user_list():
    print('1.查询所有的学生信息')
    print('2.搜索学生信息')
    print('3.增加学生信息')
    print('4.修改学生信息')
    print('5.删除学生信息')
    print('6.退出系统')
    user_input = input('输入选择的')
    return user_input

def inquire_list():
    for user in student_list:
        print(user)

def search_list():
    iput = input('输入搜索学生姓名')
    flage = False
    for user in student_list:
        if user['name'] == iput:
            flage = True
            print(user)
    if  not flage:
        print('没有搜索到学生')

def add_list():
    user_name = input('输入姓名')
    user_age = input('输入年龄')
    user_num = input('输入学号')
    student_list.append({'name':user_name,'age':user_age,'num':user_num})
    print('学生{}添加成功'.format(user_name))

def modify_list():
    iput = input('输入修改学生姓名')
    flage = False
    for user in student_list:
        if user['name'] == iput:
            flage = True
            user['name'] = input('输入修改学生姓名')
            user['age'] = input('输入修改学生年龄')
            user['num'] = input('输入修改学生学号')
            print('修改{}成功'.format(iput))
    if not flage:
        print('没有{}学生'.format(iput))

def remove_lsit():
    iput = input('输入删除学生姓名')
    flage = False
    for user in student_list:
        if user['name'] == iput:
            flage = True
            student_list.remove(user)
            print('删除{}成功'.format(iput))
    if not flage:
        print('没有{}学生'.format(iput))

def main():
    while True:
        user = user_list()
        if user in ['1','2','3','4','5','6']:
            if user == '1':
                inquire_list()
            elif user == '2':
                search_list()
            elif user == '3':
                add_list()
            elif user == '4':
                modify_list()
            elif user == '5':
                remove_lsit()
            else:
                print('再见')
                break


if __name__ == '__main__':
    main()