#、打开文件
#、w 会覆盖文件内容
file = open("NOTEPAD.TXT","w")

#、写入内容到文件
text = file.write("helo ")
print(text)

#、关闭文件
file.close()
