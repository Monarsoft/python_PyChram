def print_inf(name,gender = True):
    """
    :param name  班上同学
    :param gender :True 男生,False 女生
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"
    print("%s 是 %s" %(name,gender_text))

    return 0

print_inf("小美",True)