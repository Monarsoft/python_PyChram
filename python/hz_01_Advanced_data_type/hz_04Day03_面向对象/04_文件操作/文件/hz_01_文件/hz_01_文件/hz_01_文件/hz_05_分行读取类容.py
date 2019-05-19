fiel = open("NOTEPAD.TXT")

while True:
    tex = fiel.readline() # readline 方法只会读取一行内容，不会一次性读完而对内存占用过多
    if tex == "":  # if not tex:
        break
    print("%s" %tex,end = "")

fiel.close()
