# 使用多个键值对，存储描述一个物体的相关信息——描述跟复杂的信息
# 将多个字点放在列表中，在进行遍历
card_list = [
    {"name":"小ing",
     "age":20,
     "phone":"10086"},
    {"naem":"张三",
     "phone":"122345"}
]
print(len(card_list),type(card_list))
for card_info in card_list:

    print(card_info)