#、提示用户输入整数
try:
    integer = int(input("输入整数："))
#、使用输入的整数做除数 
    result = 8/integer

    print(result)

except ValueError:
    print("请输入正确的数！")

#、未知的错误
except Exception as result:
    print("未知错误：%s" %result )
