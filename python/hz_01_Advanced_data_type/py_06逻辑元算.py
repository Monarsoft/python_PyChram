# # 实现进入网吧上网人员都是成年人才可以海皮
# lsdkfjsl
age = int(input("刷入年龄："))
if (age >=18 and age<=120):
    print("欢迎进入海皮")
else:
    if(age >=120 or age <0):
        print("输入有误")
    else:
        print("禁止入进")