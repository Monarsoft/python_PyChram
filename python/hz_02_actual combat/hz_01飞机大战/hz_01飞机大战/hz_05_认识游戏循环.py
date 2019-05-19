import pygame
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
    #screen.blit(hero2,(175,562))
    pass
except Exception as result:
    print("error：%s" %result)


# 、游戏循环 ->游戏的开始
i = 0
while True:
    # 3、更新图像显示
    pygame.display.update()
    clock.tick(2)

    print(i)
    i +=1
pygame.quit()
