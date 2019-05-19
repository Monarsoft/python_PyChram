# 网上获取内容
#1. 去除所有空白字符
#2. 用“ ” 分割排列
pore_str = "静夜思\n\n李白\t床前明月光\n疑似地上霜\t举头望明月\n\n低头思故乡"
print("1:",pore_str)
# 1.f
pore_split = pore_str.split()
print("2：",pore_split)
# 2.
pore_join = " \n ".join(pore_split)
# for pore_join2 in pore_join:
#     print("3:",pore_join2)
print("3:", pore_join)