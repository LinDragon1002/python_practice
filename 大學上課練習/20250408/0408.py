import pygame
import sys

# 初始化 pygame
pygame.init()

# 啟用全螢幕模式
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("全螢幕畫紅色圓")

# 取得螢幕寬高
width, height = screen.get_size()

# 設定背景顏色為白色
screen.fill((92, 156, 228))

# 設定圓心座標（畫面正中央）與半徑
center = (width // 2, height // 2)
radius = 50  # 圓的半徑

# 畫出紅色圓形
pygame.draw.circle(screen, (255, 0, 0), center, radius)

# 更新畫面
pygame.display.flip()

# 遊戲主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

# 離開時釋放資源
pygame.quit()
sys.exit()