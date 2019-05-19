# 、打开文件
file_read = open("NOTEPAD.TXT") # 默认为读取 r 方式
file_write = open("NOTEPAD[复件].TXT","w+")

# 、读写文件
tex_read = file_read.read()
tex_write = file_write.write(tex_read)

# 、查看复制文件


# 、关闭文件
file_read.close()
file_write.close()
