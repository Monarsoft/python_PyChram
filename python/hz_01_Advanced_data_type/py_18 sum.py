#求两个数之和的函数

def sum_1(num1, num2):
    """求两个数的和"""
    sum = num1+num2
    #print("\n%d+%d=%d" %(num1,num2,sum))
    return sum

num1 = int(input("输入第一个数："))
num2 = int(input("输入第二个数："))

a = sum_1(num1,num2)
print("sum_result:%d" %(a))