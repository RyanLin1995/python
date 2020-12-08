import pygame
from random import randint


class Rect:

    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.width, self.height = 88, 44
        self.rect_color = (255, 255, 255)

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.x = settings.screen_width - self.width
        self.rect.y = randint(0, settings.screen_height - self.height)

        self.y = self.rect.y

    def update(self):
        self.y += self.settings.rect_speed
        self.rect.y = self.y

    def rect_check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.y >= screen_rect.height:
            self.settings.rect_speed = -1
        elif self.rect.y <= 0:
            self.settings.rect_speed = 1

    def draw_rect(self):
        self.screen.fill(self.rect_color, self.rect)
