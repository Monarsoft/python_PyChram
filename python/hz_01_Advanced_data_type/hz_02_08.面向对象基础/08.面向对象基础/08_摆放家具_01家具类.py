class HouseItem:
    
    def __init__(self,name,argea):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.argea = argea
    def __str__(self):
            # 放回家具信息
            return "【%s】 占地 %.2f 米" %(self.name,self.argea)
        

# 创建家具
chest = HouseItem("迪蒙罗",4)
table = HouseItem("餐桌",5)
print(chest)
print(table)

