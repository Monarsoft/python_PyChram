try:
    integer = float(input("输入Float类型数值："))
except Exception as integer:
    print("未知错误： %s" %integer)
    pass
else:
    print("没有任何异常！")
finally:
    print("执行完毕！")

