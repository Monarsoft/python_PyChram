xiaoming_dcit = {"name":"小明",
                 "age":19}
 #1. 统计键值对数量
print(len(xiaoming_dcit))
 #2. 合并字典
dic_x = {"phone":10086,
          "age":20}
xiaoming_dcit.update(dic_x) # 如果当前出现原有的key 那么就会覆盖原有的 键值对

 #3. 清空字典
xiaoming_dcit.clear()


print(xiaoming_dcit)