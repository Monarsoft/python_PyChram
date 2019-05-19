import random
import pygame
# 创建窗口大小
SCREEN_RECT = pygame.Rect(0,0,480,850)
# 刷新帧率 
FRAME_PER_SEC = 60
# 、创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹
HERO_FIRE_EVENT = pygame.USEREVENT +1

class GameSprite(pygame.sprite.Sprite):
    """  精灵(sprite)   """
    def __init__(self,image_name, speed=1):
        # 1、初始化父类方法
        super().__init__()
        # 2、定义属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 垂直运动
        self.rect.y += self.speed
class Backgroud(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt = False):
        # 1、 调用父类方法实现精灵的创建（image/rect/speed)
        super().__init__("./images/background.png")
        #super().__init__("./images/enemy1.png")

        # 2、 判断是否交替图像，如果是，需要设置初始化位置
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        # 1、调用父类方法

        # 2、判断是否移除屏幕，如果移除，将图像设置屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = self.rect.height
        return super().update()

class Enemy(GameSprite):
    """敌机精灵类"""
    def __init__(self):
        # 1、调用父类方法，创建敌机，同时制定敌机图
        super().__init__("./images/enemy1.png")
        # 2、指定敌机初始随即速度  1-3
        self.speed = random.randint(1,3)
        # 3、指定敌机初始位置 
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width -self.rect.width
        self.rect.x = random.randint(0,max_x)

        pass

    def update(self):
        # 1、调用父类方法，保持垂直方向飞行
        super().update()
        # 1、判断是否飞出屏幕，如果是，需要冲精灵组中删除
        if self.rect.y == SCREEN_RECT.height:
            print("删除")
            # kill方法可以将精灵从精灵族中移除，精灵就会自动销毁
            self.kill()
    def __del__(self):
        print("敌机销毁：%s" % self.rect)
        pass

class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        # 1、调用父类方法
        super().__init__("./images/hero1.png",0)
        # 2、设置英雄位置
        self.rect.centerx =SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom -120
        # 创建子弹精灵/精灵族
        #self.bullets = Bullet()
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 英雄位置水平移动
        self.rect.x = self.speed

        # 是否移除屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
       
        for i in (0, 1, 2):

            # 1、创建子弹精灵
            bullet = Bullet()
            # 2、设置精灵位置
            bullet.rect.bottom = self.rect.y -i * 20
            bullet.rect.centerx = self.rect.centerx

            # 3 、将精灵添加到精灵组
            self.bullets.add(bullet)
        
class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def __update(self):
        # 调用父类方法，让子弹垂直方向飞行
        super().update()
        # 判断子弹飞出屏幕
        if self.rect.bottom <0:
            self.kill

    def __del__(self):
        print("子弹:%s" % self.rect)