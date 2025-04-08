import random
import pygame
import sys

class circle():
    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def fall(self):
        self.y += random.randint(1,10)
        if self.y >= height:
            self.y = 0

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

# 設定圓心座標（畫面正中央）與半徑
dots = []
for _ in range(100):
    x = random.randint(0, width)
    y = random.randint(0, height)
    size = random.randint(1,100)
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    dots.append(circle(x,y,size,color))
# center = (width // 2, height // 2)
# radius = 50  # 圓的半徑



clock = pygame.time.Clock()

# 遊戲主迴圈
running = True
while running:

    # 設定背景顏色為白色
    screen.fill((92, 156, 228))

    # 畫出紅色圓形
    for d in dots:
        d.fall()
        pygame.draw.circle(screen, d.color, (d.x,d.y), d.size)

    # 更新畫面
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

# 離開時釋放資源
pygame.quit()
sys.exit()