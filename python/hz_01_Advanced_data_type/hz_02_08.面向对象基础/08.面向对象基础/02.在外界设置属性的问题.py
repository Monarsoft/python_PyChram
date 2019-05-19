class Cat:
    # 创建一个猫类 

    # 由 哪个对象 调用的方法，方法的self就是 哪个对象的引用
    def eat(self):
        print("%s爱吃鱼" %self.name)
    def drink(self):
        print("%s要喝水" %self.name)

# 创建个tom猫对象
tom = Cat()

#tom.name = "Tom"
tom.drink()
tom.eat()
#tom.name = "tom"   # Erro
