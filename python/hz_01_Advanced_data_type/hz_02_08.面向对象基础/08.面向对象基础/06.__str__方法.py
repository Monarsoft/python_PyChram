
class Cat:
    """创建一个猫类"""
    
    def drink(self):
        print("%s要喝水" %self.name)

    def __init__(self):
        print("初始化方法")
        # self.属性名 = 属性初始值
        self.name = "Tom"

    # __del__方法在对象消失是自动调用
    def __del__(self):
        print("%s 返回了" %self.name)

    # __str__方法必须要返回一个值
    def __str__(self):
        return "我是小猫 %s" %self.name

# 使用 Cat类 创建对象 ，会自动调用初始化__.init__方法
Tom = Cat()

# del 可以删除一个对象
print(Tom)
del Tom # 删除对象
print("-"*10)


"""
pydev debugger: starting

初始化方法
我是小猫 Tom
Tom 返回了
----------
Press any key to continue . . .

"""
