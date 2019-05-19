# 打印多次输出语句
import random
i = random.randint(int(input("1:")),int(input("2:")))
leng = 0
while(i == 6):
    print("(%c) %d" %(i,leng))
    leng = leng + 1
    #i = i + 1
    i += 1
    if(leng == 1000):
        break
r = 0
leng = 0
while r<5:
    r +=1
    leng +=r # 加上r每次加1的值
print("R=%d" %leng)