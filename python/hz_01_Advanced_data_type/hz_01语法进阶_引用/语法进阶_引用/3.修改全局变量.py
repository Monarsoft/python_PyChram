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


def demo3():
    # 想要修改全局变量 ，使用 global 声明变量即可
    # global 关键字告诉编译器 后面的是全局变量
    # 在用赋值语句时，就不会自动创建局部变量
    global sum

    sum = 10
    print("本函数修改:%d" %sum)
    return
def demo4():
    print("demo3修改之后的值是：%d" %sum)
    
demo1()
print("="*30)
demo2()
print("="*30)
demo3()
demo4()
