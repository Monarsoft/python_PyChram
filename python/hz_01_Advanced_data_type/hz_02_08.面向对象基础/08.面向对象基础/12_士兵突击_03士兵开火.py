class Gun:
    def __init__(self,model,colour):
        # 1. 枪的型号
        self.model = model 
        # 子弹的数量
        self.bullet_count = 0
        # 颜色
        self.colour = colour
    def __str__(self):
        return "【%s %s [子弹数量：%d发 ]】" % (self.colour,self.model,self.bullet_count)

    def add_bullet(self,count):
        # 1. 添加子弹
        self.bullet_count += count

    def shout(self):
        # 1.子弹的数量是否有
        if self.bullet_count<=0:
            print("%s 子弹用完了......" %self.model)
            return
        # 2.子弹发射    
        else:
            print("*"*10)
            print(" "*10,"%s哒哒***************[%d]" % (self.model,self.bullet_count))
            print("*"*10)
            self.bullet_count -= 1

class Soldier:
    def __init__(self,name):
        # 1.士兵姓名
        self.name = name
        # 2. 新兵-没有枪
        self.gun = None
    
    def fire(self):
        # 1. 是否有枪
        # if self.gun == None:
        if self.gun is None:
            print("【%s】没有枪。。。" % self.name)
            return 
        # 2. 发出口号
        print("冲啊。。。【%s】" %self.name)
        # 3. 装填子弹
        self.gun.add_bullet(10)
        # 4. 射击
        self.gun.shout()




Ak47 = Gun("AK47","黄金")
A569 = Gun("重加特林","银")
xusanduo = Soldier("许三多")
#xusanduo.gun = Ak47
xusanduo.gun = A569
xusanduo.fire()



print(xusanduo.gun)