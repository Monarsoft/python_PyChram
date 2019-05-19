# 1.体会input 导入模块（“工具包”）的使用
guess = int(input("输入要出的拳--石头(1) /剪刀(2) /布(3)\n"))
if(guess == 1):
    print("石头 胜 剪刀")
elif(guess == 2):
    print("剪刀 胜 布")
elif(guess == 3):
    print("布 胜 石头")
else:
    print("重新出")
system("pause")