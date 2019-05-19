list_eval = input("输入试子：")

try:
    print(eval(list_eval))

except Exception as result:
    print("name:%s" %result)
else:
    print("通过！")
finally:
    print("程序结束！")
