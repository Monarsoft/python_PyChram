#、提示用户输入整数
try:
    integer = int(input("输入整数："))
#、使用输入的整数做除数 
    result = 8/integer

    print(result)
except ZeroDivisionError:
    print("‘0’不能做除数")

except ValueError:
    print("请输入正确的数！")