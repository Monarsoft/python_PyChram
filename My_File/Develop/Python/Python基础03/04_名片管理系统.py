#coding=utf8
'''名片管理系统
'''
#1.打印提示信息
print("="*50)
print(" 欢迎使用名片管理系统 V1.0")
print("1.增加一个新的名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.列出所有名片名片")
print("0.退出名片管理系统")
print("="*50)

#定义一个存放名片的列表
cardInfos = [{"name":"小李子","phone":"1200000","email":"1200000@mail.com"},{"name":"小宝","phone":"1111111","email":"1111111@mail.com"},{"name":"小桃子","phone":"100001","email":"100001@inf.com"}]
while True:
    #2.获取用户输入
    num = int(input("请输入对应的功能："))

    #3.根据用户输入相应功能的编号
    if num in (1,2,3,4,5,0):
        # 增加名片
        if num == 1:
            new_infos = {}
            new_name  = input("输入姓名：")
            new_phone = input("输入手机号码：")
            new_email = input("输入电子邮件：")
            new_infos["name"] = new_name
            new_infos["phone"] = new_phone
            new_infos["email"] = new_email
            cardInfos.append( new_infos)

        # 删除一个名片
        elif num == 2:
            removek_infos = input("输入要删除的姓名：")
            for remove_card in cardInfos:
                if remove_card["name"] == removek_infos:
                    rm = remove_card
                    while True:
                        rminput = int(input("你真的要删除吗？1.是的\t 2.取消\n："))
                        if rminput == 1:
                            #print(rm["name"]) 
                            #cardInfos.remove(rm)
                            cardInfos.remove(rm)
                            #print(cardInfos)
                            #print(remove_card)
                            print("删除成功！")
                            break
                            #pass
                        elif rminput == 2:
                            break
                            #pass
                        else:
                            print("输入有误，请重新输入：")
                    break
            else:
                print("此人不在系统内。。。")

        # 修改一个名片
        elif num == 3:
            #用户输入需要修改的姓名
            card_modify = input("请输入需要修改的姓名：")
            num_modify = 0 #控制if没有找到则提示
            xg_num = 0
            for modify_temp in cardInfos:
                if modify_temp["name"] == card_modify:
                    num_modify == 1
                    print(modify_temp)
                    print("="*50)
                    print("1.修改姓名")
                    print("2.修改电话号码")
                    print("3.修改电子邮件")
                    print("5.退出修改")
                    print("="*50)
                    xg_num += 1

                    #提示输入需要修改的内容
                    modify_values = int(input("输入对应修改内容的编号："))
                    if modify_values == 1:
                        #cardInfos[modify_temp]["name"]
                        print("姓名修改成功！")
                        cardInfos[xg_num]["name"] = input("输入新姓名：")
                        num_modify = 1
                    elif modify_values == 2:
                        cardInfos[xg_num]["phone"] = input("输入新的手机号码：")
                        num_modify = 1
                    elif modify_values == 3:
                        cardInfos[xg_num]["email"] = input("输入新的电子邮件：")
                        num_modify = 1
                    elif modify_values == 5:
                        break
                    else:
                        print("输入有误，请从新输入！")
                    print("修改成功！")

                if num_modify == 2:
                    print("修改不成功，没有找到此人！")

        # 查询一个名片
        elif num == 4:
            find_name = input("输入要查询的姓名：")
            find_flag = 0# 默认为零没有查找到
            for temp_find in cardInfos:
                if find_name == temp_find['name']:
                    print("姓名\t\t电话\t\t邮件")
                    print("%s\t\t%s\t\t%s"%(temp_find["name"],temp_find["phone"],temp["email"]))
                    find_flag = 1
                    break
            if find_flag == 0:
                print("查无此人.....")
                
        # 列出所有名片
        elif num == 5:
            print("姓名\t\t电话号\t\t电子邮件")
            for temp in cardInfos:
                print("%s\t\t%s\t\t%s"% (temp["name"],temp["phone"],temp["email"]))
                #print(temp) # for test
            print("="*50)

        # 退出名片
        elif num == 0:
            break
    else:
        print("输入有误请从新输入！")
    print("="*50)
