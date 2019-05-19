# 注意：在开发时，应该把模块中的所有全局变量
# 定义所有函数的上方位置， 可以保证所有函数
# 都能够正常访问到每个全局变量
sum = 100

# 在定义一个全局变量
name = "小明"

# 定义个自定义函数
def demo1():
    print("sum:%d" %sum)
    print("name:%s" %title)
    print("name:%s" %name)  # NameError("name 'name' is not defined",)
    return


# 定义一个变量
title = "pywod"

## 调用demo1 函数
#demo1()

## 在定义一个全局变量
#name = "小明"
demo1()