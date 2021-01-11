import pygame


class Little_ship():
    """这里存储了飞船本体"""
    def __init__(self, setting, ship_screen):
        self.ship_screen = ship_screen
        self.setting = setting

        self.image = pygame.image.load('images/spacecraft.png')
        self.rect = self.image.get_rect()
        self.ship_screen_rect = self.ship_screen.get_rect()

        self.rect.bottom = self.ship_screen_rect.right
        self.rect.centery = self.ship_screen_rect.centery

        self.moving_up = False
        self.moving_down = False

        self.ship_centery = float(self.rect.centery)

    def little_ship_update(self):
        if self.moving_up and self.rect.top > 0:
            self.ship_centery -= self.setting.little_ship_speed
        if self.moving_down and self.rect.bottom < self.ship_screen_rect.bottom:
            self.ship_centery += self.setting.little_ship_speed

        self.rect.centery = self.ship_centery

    def blitme(self):
        self.ship_screen.blit(self.image, self.rect)