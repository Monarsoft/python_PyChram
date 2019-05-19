import pygame
from plane_sprites import *
# 、时间
clock = pygame.time.Clock()


class PlanGame(object):
    def __init__(self):
        print("初始化")
        # 1、创建窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2、创建时钟
        self.clock = pygame.time.Clock()
        # 3、调用私有方法，完成精灵和精灵族的创建
        self.__create_sprites__()
        # 4、设置定时器事件，创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
        pygame.time.set_timer(HERO_FIRE_EVENT,500)

    def __create_sprites__(self):
        bg1 = Backgroud()
        bg2 = Backgroud(True)
        print(bg1,bg2)
        #bg2.rect.y = -bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1,bg2)
        # 创建敌机精灵族
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵/精灵族
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        
        
        pass

    # 2、事件监听
    def __event_handler__(self):
        for event in pygame.event.get():
            # 判断退出游戏
            if event.type == pygame.QUIT:
                PlanGame.__game_over__()
            elif event.type == CREATE_ENEMY_EVENT:
                #print("敌机出发")
                # 创建敌机精灵
                enemy = Enemy()
                # 添加到敌机精灵族
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
 #elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("移动有")
                
            # 使用键盘提供方法获取键盘按键， 按键元组
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中按键值
            if keys_pressed[pygame.K_RIGHT]:
                print("K_Right")
                self.hero.speed +=5
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed -=5
            #else:
            #    self.hero.speed = 0

     # 3、碰撞检测
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets,self.enemy_group,True,True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True) 
        # 判断是否有内容列表
        if len(enemies) >0:
            # 1、 英雄牺牲
            self.hero.kill()
            # 2、游戏结束
            PlanGame.__game_over__()

    # 4、更新/绘制精灵族
    def __update_sprites__(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over__():
        pygame.quit()
        print("英雄光荣牺牲")
        print("游戏结束")
        exit()


    # 开始游戏
    def star_game(self):
        print("开始")
        while True:
            # 1、刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2、事件监听
            self.__event_handler__()
            # 3、碰撞检测
            self.__check_collide()
            # 4、更新/绘制精灵族
            self.__update_sprites__()
            # 5、更新显示
            pygame.display.update()



if __name__ == "__main__":
    glame = PlanGame()
    glame.star_game()

#screen = pygame.display.set_mode((600,600))
#while True:
#    clock.tick(60)
#    for event in pygame.event.get():
#        print(event)