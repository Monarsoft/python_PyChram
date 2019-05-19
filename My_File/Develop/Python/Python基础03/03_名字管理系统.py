#coding=utf8
'''
功能：名字管理系统增删改查
'''
#1.提示信息与介绍
print("="*32)
print("  欢迎使用名字管理系统(1.0版本)")
print("1.增加姓名||")
print("2.删除姓名||")

print("4.查询姓名||")
print("0.退出名字管理系统")
print("="*32)
names = ['挑子', '郝丽', '老李', '老苏', '孟浩']
while 1:
    #2.获取用户实现功能的信息
    num = int(input("请输入相应功能的编号："))

    #3.功能实现
    # 增添姓名
    if num == 1:
        newName = input("输入需要存储的姓名：")
        names.append(newName)

    # 删除姓名
    elif num == 2:
        rname = input("输入需要删除的姓名：")
        if rname in names:
            names.remove(rname)
        else:
            print("姓名不存在！")

    # 修改姓名
    elif num == 3:
        subscript = int(input("需要修改第几个的姓名，输入排行的个数:"))
        if subscript > len(names):
            print("没有下标的姓名不存在！")
        else:
            subscript -=1
            print("你要修改的姓名是%s"% names[subscript])
            names[subscript] = input("输入新的姓名：")

    # 查询姓名
    elif num == 4:
        nas = len(names)
        print("\033[%s;40m姓 名\033[0m"%(31) )
        for i in names:
            nas -= nas-1
            print("%d、%s"% (nas,i))

    # 退出程序
    elif num == 0:
        break
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
