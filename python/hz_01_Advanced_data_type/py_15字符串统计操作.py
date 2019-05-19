hello_str = "Hello python"
# 1. 统计字符串长度
print("hello_str变量中字符串长度：",len(hello_str))
# 2. 统计某个小字符串出现的次数
print('"o"字符串出现的次数：',hello_str.count("A"))
print('"o"字符串出现的次数：',hello_str.count("llo"))
# 3. 某个子字符串出现的索引（位置）
print(hello_str.index("l"))  # 如果变量中出现相同的键值对则 取最近的那个
# print(hello_str.index("g"))  # 注意 error