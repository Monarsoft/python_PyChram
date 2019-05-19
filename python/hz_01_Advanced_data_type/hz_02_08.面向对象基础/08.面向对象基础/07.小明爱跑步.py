class Person:

    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "\n我是 %s ,体重%.2fKg" %(self.name,self.weight)

    def __del__(self):
        print("%s回家了" %self.name)
    # 爱吃东西
    def eat(self):
        print("%s 爱吃东西!"% self.name)
        self.weight +=0.7
    # 爱跑步
    def run(self):
        print("%s爱跑步!" % self.name)
        self.weight -=0.5

# 创建小明对象
xiaoming = Person("小明",76.5)

xiaoming.eat()
xiaoming.run()
print(xiaoming)
del xiaoming
print("\n")
# 创建小美对象
xiaomei = Person("小美",46.1)
xiaomei.eat()

 