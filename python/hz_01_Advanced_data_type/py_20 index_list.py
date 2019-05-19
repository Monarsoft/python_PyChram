# 创建一个列表，在其他语言中为数组
list_a = ["xiaolizi","xiaoshunzi","xiaohongzi"]
print("%s" %list_a)

#0. 取值和索引
# 有了数据的下标直接取出内部的值
print("取值：",list_a[1])

#知道数据内容，想要知道数据在列表中的位置
#可以使用index方法，传入内容得出索引
print("索引：",list_a.index("xiaoshunzi"))

#1.修改
# 知道索引直接修改
list_a[2] = "小明"

#2.增加
# append 方法可以在列表末尾追加数据
list_a.append("wangsi")
#insert 方法可以在列表指定索引位置插入数据
list_a.insert(2,"ABK")
# extend 方法可以把其他完整的内容追加到当前列表末尾
temp_list = ["宗介","波鹨","淑珊","刘潇逸"]
list_a.extend(temp_list)


#3.删除
# remove方法删除指定对象
list_a.remove("xiaoshunzi")
# pop 方法默认情况下可以直接删除最后一个元素
list_a.pop()
# pop 方法也可以删除指定元素的索引
list_a.pop(2)
# clear 方法默认可以直接删除所有元素
#  list_a.clear()
print(list_a)