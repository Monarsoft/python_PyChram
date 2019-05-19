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


Ak47 = Gun("AK47","黄金")

Ak47.add_bullet(1)
print(Ak47)

Ak47.shout()
