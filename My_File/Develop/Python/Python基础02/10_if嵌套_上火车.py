#coding=utf8
'''
if嵌套，实现买麦车票
'''
print("="*19)
print("安检程序(1.0版本)")
print("="*19)

print("安检一")
ticket = input("你有票马？")
if ticket in ["有","有票","yes","Yes","有的"]:
    print("请进,去到安检二物品")
    length = int(input("你的刀有多长？(cm)"))
    if length <= 10:
        print("请上车，旅途愉快！")
    elif length >1000:
        print("你带的是锯子吧")
    else:
        print("你是那个火星来的")
else:
    print("没有票就去买票吧")
