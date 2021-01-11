import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/sun.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        self.y += (self.settings.star_speed_factor * self.settings.star_fleet_direction)
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
