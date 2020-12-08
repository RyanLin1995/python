import pygame
import sys
from pygame.sprite import Group
from rain_function import create_rains
from rain_function import update_rains


class Screen_setting():
    screen_width = 1000
    screen_height = 800
    screen_bg_color = (52, 52, 52)


# class Rain(Sprite):
#     def __init__(self, screen):
#         super().__init__()
#         self.screen = screen
#         self.image = pygame.image.load('image/rain.png')
#         self.rect = self.image.get_rect()
#         self.rect.x = self.rect.width
#         self.rect.y = self.rect.height
#
#     def blitme(self):
#         self.screen.blit(self.image, self.rect)


# def get_number_rain_x(screen_width, rain_width):
#     available_space_x = screen_width - 2 * rain_width
#     number_rain_x = int(available_space_x / 2 * rain_width)
#     return number_rain_x
#
#
# def get_number_rain_y(screen_height, rain_height):
#     available_space_y = screen_height - 2 * rain_height
#     number_rain_y = int(available_space_y / 2 * rain_height)
#     return number_rain_y
#
#
# def create_rain(screen, rains, rain_list_numger, rain_row_number):
#     rain = Rain(screen)
#     rain_width = rain.rect.width
#     rain_height = rain.rect.height
#     rain.x = rain_width + 2 * rain_width * rain_row_number
#     rain.y = rain_height + 2 * rain_height * rain_list_numger
#     rain.rect.x = rain.x
#     rain.rect.y = rain.y
#     rains.add(rain)
#
#
# def create_rains(screen, screen_width, screen_height, rains):
#     rain = Rain(screen)
#     number_rain_x = get_number_rain_x(screen_width, rain.rect.width)
#     number_rain_y = get_number_rain_y(screen_height, rain.rect.height)
#     for number_y_rain in range(number_rain_y):
#         for number_x_rain in range(number_rain_x):
#             create_rain(screen, rains, number_y_rain,number_x_rain)


def rain_run():
    pygame.init()
    screen = pygame.display.set_mode(
        (Screen_setting.screen_width, Screen_setting.screen_height))
    pygame.display.set_caption('Rain')

    rains = Group()
    create_rains(screen, Screen_setting.screen_width,Screen_setting.screen_height, rains)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(Screen_setting.screen_bg_color)
        rains.draw(screen)
        update_rains(screen, rains)

        pygame.display.flip()


rain_run()
