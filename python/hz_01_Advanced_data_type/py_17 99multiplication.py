# 99 乘法口诀表函数
def wo(a):
    i = 1
    while i<=a:
        r =1
        while i>=r:
            print("%d*%d=%d" %(r,i,i*r) ,end="\t")
            r +=1
        print("")
        i +=1

a = int(input(":"))
wo(a)  #函数调用