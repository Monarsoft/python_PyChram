poem = ["望明月",
           "李白",
           "床前明月光\n\t",
           "疑似地上霜",
           "举头望明月",
           "低头思故乡\t"]
# for li_poem in poem:
#     print("|%s|" %li_poem.lstrip().ljust(10))    # 左对齐
# for li_poem in poem:
#     print("|%s|" % li_poem.strip().rjust(10, " "))  # 右对齐
for li_poem in poem:
    print("|%s|" % li_poem.strip().center(10))  # 居中对齐 去除文本中左右的空白字符