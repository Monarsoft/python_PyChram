# 导入随机工具包
import random
import py_09if嵌套火车站
# 比较胜负
# 1 剪刀 胜 布
# 2 布   胜 石头
# 3 石头 胜 剪刀
computer = random.randint(1, 3)
player = int(input("猜拳游戏 ：剪刀(1) /布(2) /石头(2)\n"))
print("玩家出的拳头是%d " %player)
if(computer == 1):
    print("Computer出的拳头是 剪刀%d" %computer)
elif(computer == 2):
    print("Computer出的拳头是 布%d" %computer)
elif(computer == 3):
    print("Computer出的拳头是 石头%d" %computer)
else:
    print("\n")
if((player == 1 and computer == 2)
        or(player == 2 and computer == 3)
        or(player == 3 and computer == 1)):

    print("你太棒了！")
elif (player == computer):
    print("平局/继续")
else:
    print("再来一局")
print(computer)