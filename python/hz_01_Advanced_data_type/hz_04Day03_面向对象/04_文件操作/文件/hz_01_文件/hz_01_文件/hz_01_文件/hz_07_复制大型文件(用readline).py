# 、打开文件
file_readline = open("NOTEPAD.TXT","r")
file_write = open("NOTEPAD【大文件】.TXT","w")

# 、读、写文件
while True:
    text_readline = file_readline.readline()
    #、判断是否读取了类容
    if not text_readline:
        break
    text_write = file_write.write(text_readline)

# 、关闭文件
file_readline.close()
file_write.close()