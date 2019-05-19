# 打印三角
# *******
# ******
# *****
# ****
# ***
# **
# *

i = 1
while i < 9:
    d = 1
    while d < i:
        print(" ", end="")
        d += 1
    r = 9
    while r > i:
        print("* ", end="")
        r -= 1
    print("")
    i += 1
