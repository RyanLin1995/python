import pygame
from pygame.sprite import Sprite
from random import randint


class Ball(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.x = randint(0, settings.screen_width)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.ball_drop_speed
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)