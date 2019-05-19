#coding=utf8
'''
功能：名字管理系统增删改查
'''
#1.提示信息与介绍
print("="*32)
print("  欢迎使用名字管理系统(1.0版本)")
print("1.增加姓名||")
print("2.删除姓名||")
print("3.修改姓名||")
print("4.查询姓名||")
print("5.退出名字管理系统")
print("="*32)
while True:
        #2.获取用户实现功能的信息
        num = int(input("请输入相应功能的编号："))

        #3.功能实现
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
        else:
            print("-"*50)
            print("输入有误，请从新输入!")






'''
names = ["桃子","李杜","阛阓"]
print("-"*80)
print("1.查询、2.修改、3.删除、0.退出")
ifs = input("请输入需要的操作：")
print("-"*80)

# 是否正确输入
if ifs in ("查询","修改","删除","退出"):
    if ifs == "查询":
        if names == []:
            print("没有记录！")
        else:
            print("姓名")
            print("-"*80)
            for i in names:
                print(i)
    elif ifs == "修改":
        pass
    elif ifs == "删除":
        names.remove(input("输入需要删除的姓名:"))
    else:
        pass
            
print("-"*80)
'''
