work_list = list()
# work_list = [{
#     "name": "lzd",
#     "identify": "123456789123456789",
#     "id": "00001"
# }, {
#     "name": "lzd",
#     "identify": "123456789123456789",
#     "id": "00002"
# }]


def identify_check(id_num):
    identify_list = list()
    for temp_dict in work_list:
        identify_list.append(temp_dict['identify'])
    if id_num in identify_list:
        print('身份证输入重复')
        return False
    if len(id_num) != 18 or not(id_num.isalnum() or id_num.decimal()):
        print('身份证输入信息无效')
        return False
    else:
        return True


def id_check(id_num):
    id_list = list()
    for temp_dict in work_list:
        id_list.append(temp_dict["id"])

    if len(id_num) != 5:
        print('id为5位')
        return False

    return True


def name_check(name):
    if name:
        return True
    else:
        print("姓名无效")
        return False


def show_info(info_list):
    if len(info_list):
        print("欢迎员工系统\n\n姓名\t\t\t\t身份证\t\t\t\t\t\tID号\n"+"-"*60)
        print(info_list)
        for work_dic in info_list:
            print("{}\t\t\t{}\t\t\t{}\n".format(work_dic["name"], work_dic["identify"], work_dic["id"]))
    else:
        print("系统内信息为空")


print("*" * 20 + "职工管理系统" + "*" * 20 + "\n")
while True:
    name_flag = False
    id_flag = False
    no_flag = False
    order = input("*" * 25 + "\n>1.信息录入\n>2.查看信息\n>3.根据索引查询员工\n>0.退出")
    if order == '1':
        while not name_flag:
            name = input('输入姓名')
            name_flag = name_check(name)
        while not id_flag:
            identify = input('输入身份证')
            id_flag = identify_check(identify)
        while not no_flag:
            id = input('输入ID')
            no_flag = id_check(id)
        work_list.append({"name": name, "identify": identify, "id": id})
    elif order == '2':
        show_info(work_list)
    elif order == '3':
        str = input("输入相关信息")
        query_list = list()
        for dict_info in work_list:
            for k, v in dict_info.items():
                if name in v:
                    index = work_list.index(dict_info)
                    query_list.append(work_list[index])
                    break
        show_info(query_list)
    elif order == '0':
        print("已退出")
        break
    else:
        print(order+"输入错误")





