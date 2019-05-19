def input_password():
    #1 提示用户输入密码
    pwp = input("输入密码:")
    #2 判断密码长度 >=8 ，返回密码
    if len(pwp) >= 8:
        return pwp
    #3 密码长度 <8 ，主动抛出
    print("len error")
    #4 创建异常对象
    ex = Exception("请输入不少于8位数")
    #5 抛出异常
    raise ex

# 用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)