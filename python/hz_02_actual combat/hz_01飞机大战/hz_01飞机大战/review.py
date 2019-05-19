# 导入包（pygame）
import pygame
pygame.init()  # 初始哈pygaem所有工具
colock = pygame.time.Clock()
G_LEN = 4

#@staticmethod
def main():
    # 创建窗口 480 * 850
    screen = pygame.display.set_mode((480,850),0,0)

    # 加载图像
    background = pygame.image.load("./images/background.png")
    hero = pygame.image.load("./images/hero1.png")
    enemy = pygame.image.load("./images/enemy1.png")
    #enemy_group = pygame.sprite.Group(enemy)
    #hero_group = pygame.sprite.Group(hero)
    #pygame.sprite.spritecollide(hero_group,enemy_group,True)

    # 绘制图像
    screen.blit(background,(0,0))
    screen.blit(hero,(300,600))
    screen.blit(enemy,(270,100))

    # 刷新图像显示
    pygame.display.update()

    # 使用键盘提供方法获取键盘按键， 按键元组
    keys_pressed = pygame.key.get_pressed()

    # 获取飞机位置
    her_rect = pygame.Rect(300,600,102,126)
    enemy_rect = pygame.Rect(270,100,57,43)


    # 游戏循环
    while True:
        colock.tick(60)
        # 事件监听
        #for event in pygame.event.get():
        #    print(event)
        keys_pressed = pygame.key.get_pressed()
        for evt in pygame.event.get():
            print(evt)
            if pygame.QUIT == evt.type:
                print("游戏结束")
                pygame.quit()
                exit()
        #判断是否向右
        if keys_pressed[pygame.K_RIGHT]:
            print(her_rect.x)
            her_rect.x +=G_LEN
        # 判断是否向左
        elif keys_pressed[pygame.K_LEFT]:
            her_rect.x -=G_LEN
            print(her_rect.x)
        elif keys_pressed[pygame.K_DOWN]:
            print(her_rect.y)
            her_rect.y +=G_LEN
        elif keys_pressed[pygame.K_UP]:
            print(her_rect.y)
            her_rect.y -=G_LEN
    
        if keys_pressed[pygame.K_w]:
            enemy_rect.y +=G_LEN
        elif keys_pressed[pygame.K_s]:
            enemy_rect.y -= G_LEN
        elif keys_pressed[pygame.K_a]:
            enemy_rect.x -=G_LEN
        elif keys_pressed[pygame.K_d]:
            enemy_rect.x +=G_LEN

        # 判断是否飞出屏幕
        if her_rect.y < -126:
            her_rect.y = 850
        elif her_rect.y > 850:
            her_rect.y = -126
        # 碰撞
        #pygame.sprite.spritecollide(hero,enemy,True)

        screen.blit(background,(0,0))
        screen.blit(enemy,enemy_rect)
        screen.blit(hero,her_rect)
    
        pygame.display.update()
        pass

    pygame.quit()

main()