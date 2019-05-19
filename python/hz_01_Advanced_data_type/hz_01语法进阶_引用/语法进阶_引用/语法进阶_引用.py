def test(sum):
    print("在函数内部 %d 对应的内存地址是: %d" %(sum,id(sum)))

    # 1. 定义一个字符变量
    result = "Hello"

    print("函数要返回数据的内存地址是: %d" %(id(result)))

    # 将字符串返回给函数
    return result

# 定义个个a变量
a = 10
t = test(a)
print("%s 的内存地址为：        %d" %(t, id(t)))