def print_inf(name,title = "",gender = True): # 没初始化的参数需要定义在前面
    """
    :param name  班上同学
    :param gender :True 男生,False 女生
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"
    print("[%s] %s 是 %s" %(title,name,gender_text))

    return 0

print_inf("小李")    
print_inf("小美",gender=False) # 需要给哪个传参 就指定形参
