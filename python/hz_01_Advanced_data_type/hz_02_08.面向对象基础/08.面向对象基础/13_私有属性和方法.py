class Women:
    
    def __init__(self,name):
        self.name = name
        self.__age = 18

    def __secret(self):
        #在对象方法中是可以访问私有属性的
        print("%s 的年龄是%d" %(self.name,self.__age))



xiaofang = Women("小芳")

# 私有的方法，外部不能调用
xiaofang.__secret()
# 私有的属性，外界不能访问
print(xiaofang.__age)