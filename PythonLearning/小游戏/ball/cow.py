import pygame
from pygame.sprite import Sprite


class Cow(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/cow.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)

        self.moving_letf = False
        self.moving_right = False

    def update(self):
        if self.moving_letf and self.rect.left >= 0:
            self.centerx -= self.settings.cow_speed
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.centerx += self.settings.cow_speed

        self.rect.centerx = self.centerx

    def center_cow(self):
        self.centerx = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)



