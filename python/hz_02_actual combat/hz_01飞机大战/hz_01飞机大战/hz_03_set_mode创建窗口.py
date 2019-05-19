import pygame
pygame.init()

# 1、创建游戏窗口 480 * 852
screen = pygame.display.set_mode((480,852))
print(screen)


while True:
    pygame.display.update()
pygame.quit()
