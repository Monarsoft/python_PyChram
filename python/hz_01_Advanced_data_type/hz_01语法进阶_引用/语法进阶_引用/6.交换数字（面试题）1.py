# 交换两个数的位置
a = 100
b = 10
print("%d %d" %(a,b))

# 1. 使用 ^ 符号
#a = a^b
#b = a^b
#a = a^b

# 2. 使用一个变量
r = a
a = b
b = r

# 3.不使用 其他变量
#a = a+b
#b = a-b
#a = a-b


# 4.使用python 专用方法
a,b = (b,a)


print("%d %d" %(a,b))

