#coding=utf8
'''
实现石头剪刀布
步骤：
1、提示用户输入
2、判断用户输入的是否相同，然后提示并输出
3、错误则提示，并结束程序或重新开始
'''
sun = 32
import random
print("="*sun)
print("石头剪刀布(版本1.0)")
print("石头(1)、剪刀(2)、布(3)、exit(0)")
print("="*sun)

'''
player = int(input("输入需要出的："))
print(computer)
if player in (1,2,3):
    if player >computer:
        if player == 1:
            print("恭喜通过！好羡慕哦2.1")
        elif player == 2:
            print("2.2")
        else:
            print("2.2过了%d"% computer())
    elif player < computer:
        if player == 1:
            print("恭喜通过！好羡慕哦3")
        elif player == 2:
            print("过来3.1")
    else:
        print("恭喜通过！好羡慕哦1")
else:
    print("你出的是什么呢")
'''
while 1:
    computer = random.randint(1,3)
    
    print("="*sun)
   # print("")
    player = int(input("输入需要出的："))
    
    # Game entrance
    if (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):
        print("赢了，可以买奶喝了")
    elif computer == player:
        print("平局，有一手，继续")
    else:
        print("输了,有空来再来！")
    if player == 0:
        break
    #print("")
    print("="*sun)
    
