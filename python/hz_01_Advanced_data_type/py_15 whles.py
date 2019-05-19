# 打印三角形

i = 1
while i < 10:
    # print("*" *i)
    r = 1
    while i > r:
        print("%d" % r, end="")
        r += 1
    print("")
    i += 1
