#coding=utf8
'''
打印三角形如下：
*
**
***
****
*****
'''

i = 1

while i < 9:
    j = 9
    while j>i:
        #输出*
        print("-", end="")
        j -= 1
    y = 0
    while y<i:
        print("*", end="")
        y +=1

    #控制循环次数
    i += 1
    #用于换行
    print("")
