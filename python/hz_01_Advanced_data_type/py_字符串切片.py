# 字符串切片  字符串[开始索引:结束索引:步长]
sum_str = "0123456789"
# 1.截取从 2 ~ 5 位置 的字符串
print(sum_str[2:6])
# 2.截取从 2 ~ 末尾 的字符串
print(sum_str[2:])
# 3.截取从 开始 ~5 位置的字符串
print(sum_str[:6])
# 4.截取完整的字符串
print(sum_str[:])
# 5.从开始位置，每隔一个字符截取字符串
print(sum_str[::2])   # 步长 从第二个开始
# 6.从索引 1 开始，每隔一个取一个
print(sum_str[1::2])
# 7.截取从 2~末尾 -1的字符串
print(sum_str[2:-1:])
# 8.截取字符串末尾两个字符
print(sum_str[8:])
print(sum_str[-2::])
# 9.字符串的逆序（面试题）
print(sum_str[::-1])
print(sum_str[-1::-1])


sum_str = "1234567890"

sum_str[2:6]
print(sum_str)