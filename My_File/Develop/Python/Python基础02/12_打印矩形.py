#coding=utf8
'''
while循环打印矩形
'''
'''
leng = 1
# 外部循环用来控制行数
while leng < 5:
    sums = 0
    suma = 5
    #打印一个空格的倒着的三角形
    while  suma >leng:
        print(" ", end="")
        suma -=1
    #打印一个正的三角型，※代替
    while sums <leng:
        print("**",end="")
        sums += 1
    leng +=1
    print("")
'''
i = 1

while i < 5:
    j = 5
    while j > 0:
        print("*", end="")
        j -=1
    i +=1
    print("")