len_list=["5往往","1zhongsan","4中介","3帛琉","2红烛"]
len_sum=len(len_list)         #
print("列表元素有%d个"%len_sum)
print("索引为:",len_list.index("1zhongsan"))
len_list.insert(0,"6梦里")    #指定位置插入
len_list.append("7Append")   #末尾追加一条记录
len_extend=["9New","Nw"]
len_list.extend(len_extend)  # 把其它列表中的元素追加到末尾
len_list.pop(4)              #删除列表中指定位置的记录 ，默认删除最后添加的记录
len_list.remove("1zhongsan") #删除列表中指定数据
#len_list.clear()             #删除列表中所有记录
len_list.sort()              #升序排列
len_list.sort(reverse=True)  #降序排列
len_list.reverse()           #反转排列
print("成员：",len_list)

list_age=["df","df",9,93.3]
print(list_age)

for my_name in len_list:
    print("My_name:",my_name)
