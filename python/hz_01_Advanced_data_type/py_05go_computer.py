# 判断是否可以进入
age = int(input("输入年龄："))
if (age>=18 and age<200):
    print("可以进入")
if(age>200 or age <=0):
        print("输入有误，重新输入")
else:
    print("禁止入内")
