# coding:utf-8
# @FileName: 购物车.py
# @Author  :辰晨
# @Time    :2019/4/13 9:48


parice_list = [
    {'name': 'mac', 'prc': 800},
    {'name': 'book', 'prc': 400},
    {'name': 'bike', 'prc': 100}
]
# parice_list = [
#     ('mac', 800),
#     ('book',400),
#     ('bike', 100)
# ]
shopping = []
saving = input('please your saving:')
if saving.isdigit():
    saving = int(saving)
    while True:
        # enumerate 加序号 （，）逗号后面是定从几开始
        for i, v in enumerate(parice_list, 1):
            print(i, v)
        choice = input('选择购买编号【退出：q】：')
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(parice_list):
                item = parice_list[choice - 1]
                if item['prc'] < saving:
                    saving -= item['prc']
                    shopping.append(item)
                else:
                    saving -= item['prc']
                    print('钱不够差%s' % saving)
                print(item)
            else:
                print('错误')
        elif choice == 'q':
            print('bai')
            sec = 1
            for i in shopping:
                for j in shopping:
                    if i == j:
                        sec += 1
                        shopping.remove(j)
                    print(i, sec)

            break
        else:
            print('')
