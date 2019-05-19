# 全局变量使用
sum = 100

def demo1():
    print("demo1 使用全局变量:%d" %sum)
    print("id = %d" %id(sum))
    return sum

def demo2():
    print("demo2函数使用全局变量：%d" %sum)
    print("id = %d" %id(sum))
    return sum


def su():
    sum = 10
   # 全局变量sum， 所有的函数都可以使用 
   # 但是在python中不允许直接修改全局变量的值
   # 如果用赋值语句修改，则会默认在函数内部，定义一个和局部变量相同的局部变量 sum = 10
    print("su:%d" %sum)

demo1()
print("="*30)
demo2()
print("="*30)
su()