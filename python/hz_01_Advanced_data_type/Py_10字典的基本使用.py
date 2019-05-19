# 字典的增删改查
from typing import Dict, Union

xiaoming_dict = {"name": "小米", }
# 1 查找字典中的键值对,指定key
print(xiaoming_dict["name"])
# 2修改字典增加
xiaoming_dict["name"] = "小明"  # 如果key 存在就会修改键值对
xiaoming_dict["age"] = 19  # 如果key 不存在则增加键值对
# 3删除数据
xiaoming_dict.pop("age")

print(xiaoming_dict)
