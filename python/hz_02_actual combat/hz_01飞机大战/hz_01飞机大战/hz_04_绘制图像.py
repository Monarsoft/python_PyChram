import pygame

# 创建 480 *852 窗口
screen = pygame.display.set_mode((480,752))

# 1、绘制背景图像
# 2、加载图像
background = pygame.image.load("./images/background.png")
hero1 = pygame.image.load("./images/hero1.png")
hero2 = pygame.image.load("./images/hero2.png")
print(background)
#  、绘制图像
try:
    screen.blit(background,(0,0))   # 、绘制background图像
    screen.blit(hero1,(175,562))    # 、绘制Here图像
    #screen.blit(hero2,(175,562))
    pass
except Exception as result:
    print("error：%s" %result)



# 3、更新图像显示
pygame.display.update()
# 、游戏循环
while True:
    pass
pygame.quit()
