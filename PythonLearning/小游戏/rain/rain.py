import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('image/rain.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.top <= 0:
            return True
        if self.rect.bottom >= screen_rect.bottom:
            return True

    def update(self):
        self.y += 1
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)