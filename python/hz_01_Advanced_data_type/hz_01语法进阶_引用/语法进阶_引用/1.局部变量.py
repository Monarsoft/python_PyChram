def demo():
    # 局部变量分配的内存被使用完之后会被回收
    demo1 = 10
    print("Demo1变量的值：%d" %demo1);
    return demo1;
def demo2():
    demo1 = 100;
    print("Demo2函数中==>%d" %demo1);
    return demo1;


# 在函数内部定义的变量不能在其他位置使用
# 
# print(demo1) # error
demo();
demo2();