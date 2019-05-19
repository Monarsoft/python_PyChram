#coding=utf8
'''
while循环嵌套实现九九乘法表
'''

i = 1 # 用于控制行数
#用来控制行数
while i<=9:
    j = 1
    # 用于控制每行的个数
    while j<=i:
        #print(j,"*",i,"=",i*j,end="")#这样写不够规范
        print("%d*%d=%d\t"% (j,i,i*j),end="")
        j +=1
    print("")
    i +=1
