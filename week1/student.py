
class StudentSym():

    def __init__(self):
        self.student_list = []
        f = open('student','r',encoding='utf8')
        data = f.read()
        self.student_list.append(data)

    def user_info(self):
        print('*'*20)
        print('1.查询所有的学生信息')
        print('2.搜索学生信息')
        print('3.增加学生信息')
        print('4.修改学生信息')
        print('5.删除学生信息')
        print('6.退出系统')
        print('*' * 20)
        user_input = input('输入选择的')
        return user_input

    def inquire_list(self):
        for user in self.student_list:
            print(user)


    def search_list(self):
        iput = input('输入搜索学生姓名')
        flage = False
        for user in self.student_list:
            if user['name'] == iput:
                flage = True
                print(user)
        if not flage:
            print('没有搜索到学生')

    def add_list(self):
        user_name = input('输入姓名')
        user_age = input('输入年龄')
        user_num = input('输入学号')
        self.student_list.append({'name': user_name, 'age': user_age, 'num': user_num})
        print('学生{}添加成功'.format(user_name))

    def modify_list(self):
        input = input('输入修改学生姓名')
        flage = False
        for user in self.student_list:
            if user['name'] == input:
                flage = True
                user['name'] = input('输入修改学生姓名')
                user['age'] = input('输入修改学生年龄')
                user['num'] = input('输入修改学生学号')
                print('修改{}成功'.format(input))
        if not flage:
            print('没有{}学生'.format(input))

    def remove_lsit(self):
        iput = input('输入删除学生姓名')
        flage = False
        for user in self.student_list:
            if user['name'] == iput:
                flage = True
                self.student_list.remove(user)
                print('删除{}成功'.format(iput))
        if not flage:
            print('没有{}学生'.format(iput))


    def main(self):
        while True:
            user = self.user_info()
            if user in ['1', '2', '3', '4', '5', '6']:
                if user == '1':
                    self.inquire_list()
                elif user == '2':
                    self.search_list()
                elif user == '3':
                    self.add_list()
                elif user == '4':
                    self.modify_list()
                elif user == '5':
                    self.remove_lsit()
                else:
                    f = open('student','w',encoding='utf8')
                    f.write(str(self.student_list))
                    f.close()
                    print('再见')
                    break


if __name__ == '__main__':
    studen_sym = StudentSym()
    studen_sym.main()