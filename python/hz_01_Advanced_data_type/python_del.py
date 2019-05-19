# del 关键字用法(delte)
del_name = ["zhangsan","lisi","wangwu","wangwu"]
# sort() 方法把元素升序排列
del_name.sort()
# 降序排列
del_name.sort(reverse=True)
#   reverse 方法用于列表元素反转排列
del_name.reverse()
# del 关键字是把变量从内存中释放
del del_name[1]
print(del_name)
name="xiaoming"
print(name)
# len (lenth) 函数统计列表中的个数
len_list = len(del_name)
print(len_list);
# count 方法统计列表中元素出现的个数
count = del_name.count("wangwu")
print(count)