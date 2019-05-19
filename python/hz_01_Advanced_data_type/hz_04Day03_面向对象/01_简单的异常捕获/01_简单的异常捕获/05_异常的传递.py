#、异常的传递，一直传递到print()函数，如果没有解决，就会停止程序
def sum():
    return int(input("输入整数："))
def sum2():
    return sum()

try:
    print(sum2())
except Exception as result:
    print("未知错误！")
else:
    print("完美执行！")
print(type(sum2()))
