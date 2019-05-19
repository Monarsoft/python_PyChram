#coding=utf8
'''名片管理系统
'''
#1.打印提示信息
print("="*50)
print(" 欢迎使用名片管理系统 V1.0")
print("1.增加一个新的名片")
print("2.删除一个名片")
print("3.修改名片")
print("4.查询名片")
print("5.查看名片")
print("0.退出名片管理系统")
print("="*50)

while True:
    #2.获取用户输入
    num = int(input("请输入对应的功能："))

    #3.根据用户输入相应功能的编号
    if num in (1,2,3,4,5,0):
        if num == 1:
            pass
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            pass
        elif num == 5:
            pass
        elif num == 0:
            break
    else:
        print("输入有误请从新输入！")

