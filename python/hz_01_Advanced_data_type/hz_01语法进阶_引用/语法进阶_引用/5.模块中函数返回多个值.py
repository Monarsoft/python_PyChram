def measure():
    """测量水高和水压"""
    print("水高测量..")
    tall = 10
    print("测量水压..")
    pressure = 30
    
    # 元组能包含多个数据， 因此可以使用元组然函数返回多个值
    # 返回 的元组括号可以省略
    # return (tall,pressure)
    return tall,pressure

result = measure()
print("结果为:",result)


# 如果要对返回值 单独使用可以用多个变量接收
# 不建议用下标 不利于使用
# 注意：使用多个变量接收是要以返回元组的个数，保持一致
gl_tall,gl_pressure = measure()
#gl_tall =result[0]
print("gl_tall:%d" %gl_tall)
#gl_pressure = result[1]
print("gl_pressure:%d" %gl_pressure)