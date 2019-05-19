class HouseItem:
    
    def __init__(self,name,argea):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.argea = argea
    def __str__(self):
            # 放回家具信息
            return "【%s】 占地 %.2f 米" %(self.name,self.argea)        

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type        # 户型
        self.area = area                   # 总面积
        self.free_area = area               # 剩余面积
        self.item = []                     # 家具名称

    def __str__(self):
        return "户型：[%s]\n 总面积：%.3f  [剩余面积：%.3f]\n 家具：%s" %(self.house_type,self.area,self.free_area,self.item)

    def add_item(self,add_item):

        print("要添加：%s" %add_item)
        # 1.判断家具占地面积
        if add_item.argea>self.free_area:
            print("%s家具面积太大，无法添加" %add_item.name)
            return 

        # 2.将家具添加到房子中（列表)
        self.item.append(add_item.name)
        # 3.计算剩余面积
        self.free_area -= add_item.argea
        print("-"*100)


# 创建家具
chest = HouseItem("迪蒙罗",4)
table = HouseItem("餐桌",5)
#print(chest)
#print(table)

# 创建房子
My_house = House("两室一厅",60)

#添加家具
My_house.add_item(chest)
My_house.add_item(table)
print(My_house)