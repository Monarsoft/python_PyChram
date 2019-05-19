hello_str = "Hello python word"
# 1. 判断是否指定字符串开始
print(hello_str.startswith("Hello"))
# 2. 判断是否指定字符串结束
print(hello_str.endswith("word"))
# 3. 查找指定字符串
# 同 index() 指定字符串不存在则会报错
# find() 指定字符不存在则返回 -1
print(hello_str.find("python"))
# 4. 替换字符串
print(hello_str.replace("word","word's"))  # replace() 不会修改原有字符而是返回新的字符串
print(hello_str)