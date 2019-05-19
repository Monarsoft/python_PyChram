import pygame
import read
pygame.init()

# （对象） 创建 480 *852 窗口
screen = pygame.display.set_mode((480,752))
clock = pygame.time.Clock()     # \创建时钟对象

# 、绘制背景图像
# 2、加载图像
background = pygame.image.load("./images/background.png")
hero1 = pygame.image.load("./images/hero1.png")
hero2 = pygame.image.load("./images/hero2.png")
enemy1 = pygame.image.load("./images/enemy1.png")
print(background)
#  、绘制图像
try:
    screen.blit(background,(0,0))   # 、绘制background图像
    screen.blit(hero1,(175,500))    # 、绘制Here图像
    screen.blit(enemy1,(280,200))
    screen.blit(hero2,(175,500))
    pass
except Exception as result:
    print("error：%s" %result)

# 3、更新图像显示
pygame.display.update()

# 、定义rect记录飞机初始化位置
hero_rect = pygame.Rect(175,500,120,126)
enemy1_rect = pygame.Rect(280,200,57,43)
# 、游戏循环 ->游戏的开始
while True:
    clock.tick(60)
    # 1、修改飞机位置
    #hero_rect.y -=2
    enemy1_rect.y +=2
    # 、判断飞机的位置
    read.py_rect(enemy1_rect,43)
    if hero_rect.y < -126:
        hero_rect.y = 752
    # 2、调用blit 绘制
    screen.blit(background,(0,0)) # 重新绘制背景遮盖移动后的飞机
    screen.blit(hero1,hero_rect)
    screen.blit(enemy1,enemy1_rect)
    #screen.blit(hero2,hero_rect)
    # 3、调用update更新显示
    pygame.display.update()
   
pygame.quit()


