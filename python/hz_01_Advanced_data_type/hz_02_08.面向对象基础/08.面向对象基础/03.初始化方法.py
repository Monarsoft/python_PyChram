class Cat:
    """创建一个猫类"""
    
    # 初始化方法
    def __init__(self):
        print("初始化方法")

        # self.属性名 = 属性初始值
        self.name = "Tom"
    def drink(self):
        print("%s要喝水" %self.name)

# 使用 Cat类 创建对象 ，会自动调用初始化__.init__方法
Tom = Cat()
Tom.drink()
