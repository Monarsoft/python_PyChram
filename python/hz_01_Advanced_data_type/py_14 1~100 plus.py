    # 计算1~100之间偶数累计结果
i = 0
result = 0
while i<=100:
    if i%2 == 0:
        print("%d" %i)
        result +=i
    i +=1
print("1~100之间偶数累计结果是：%d" %result)

