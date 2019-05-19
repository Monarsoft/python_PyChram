import cards_tools
len = 0
while True:
    cards_tools.Cue()
    action_sts = input("请输入需要执行的操作：")
    print(action_sts)

    if action_sts in ["New","new","Browse","browse","inquiry","Inquiry","exit","Exit"]:
        print("执行的操作是：【%s】%s" %(action_sts,type(action_sts)))

        # TODO 1、 新增名片
        if action_sts in ["New","new"]:
            print("插入名片")

        # 2、查询所有名片
        elif action_sts in ["Browse","browse"]:
            print("查所有名片")

        # 3、修改名片
        elif action_sts in ["Inquiry","inquiry"]:
            print("修改名片")

        # 4、退出系统
        elif action_sts in ["Exit","exit"]:
            print("退出系统")
            break
            exit()
    else:
        print("没有这项操作")
        len +=1
        if len >10:
            print("您已输入错误次数过多，请稍后在输入！")
            exit()
        
        