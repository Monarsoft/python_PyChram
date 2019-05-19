#coding=utf8
'''
if 的嵌套使用，实现选择对象
'''
print("========================================")
print("Python 对象程序(1.0版本)")
print("========================================")
gender = input("请输入您的性别(默认为中性)：")
if gender == "男":
    print("百福美")
elif gender == "女":
    print("高复苏爱")
elif gender == "":
    print("去泰国把")
else:
    print("你的性别亭别致阿。。。")
