#coding=utf8
'''
while嵌套中的break的规则
'''
i = 0

while i < 10:
    j = 0
    while j <= i:
        print("*",end="")
        j += 1
         # 注意：break只与它相邻while配对使用，continue也是一样
        # break # break 是结束整个while循环
        continue # continue 是结束本次循环，跳转到while继续判断
        
    i += 1
    print("")
#没有break的结果
'''
*
**
***
'''

#有break的时候的结果
'''
*
*
*
'''
