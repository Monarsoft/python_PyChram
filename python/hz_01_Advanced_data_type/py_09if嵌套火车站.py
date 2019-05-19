# 火车站安检
has_ticket = input("是否有票：")
if(has_ticket == "有"):
    knife_leng = int(input("安检，带的刀有多长? 单位：厘米\n"))
    if(knife_leng >20):
        print("刀超过了20厘米长不允许带上车")
    elif(knife_leng <1):
        print("你傻了吗？")
    else:
        print("安检通过")
else:
    print("如果没有车票，不允许进入，请先买票！")