import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, little_ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.center = little_ship.rect.center
        self.rect.right = little_ship.rect.right
        self.color = settings.bullet_color
        self.bullet_speed_factor = settings.bullet_speed_factor

        self.x = float(self.rect.x)

    def update(self):
        """向右移动子弹"""
        # 更新表示子弹位置的小数值
        self.x += self.bullet_speed_factor
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)