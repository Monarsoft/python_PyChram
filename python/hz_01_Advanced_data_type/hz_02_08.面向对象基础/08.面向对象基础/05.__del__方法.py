class Cat:
    """创建一个猫类"""
    
    def __init__(self):
        print("初始化方法")

        # self.属性名 = 属性初始值
        self.name = "Tom"
    def drink(self):
        print("%s要喝水" %self.name)

    # __del__方法在对象消失是自动调用
    def __del__(self):
        print("%s 返回了" %self.name)

# 使用 Cat类 创建对象 ，会自动调用初始化__.init__方法
Tom = Cat()
print("_"*10)

# del 可以删除一个对象
del Tom  
print("-"*10)

"""pydev debugger: starting

初始化方法
我是小猫 Tom
Tom 返回了
----------
Press any key to continue . . .

"""
