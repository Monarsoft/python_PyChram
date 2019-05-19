# 、打开文件
notepad = open("NOTEPAD.TXT")

# 、读取文件内容
text = notepad.read()
print(text)
print(len(text))

# 、关闭文件
notepad.close()
print(len(text))


