import sys
import pygame
from pygame.sprite import Group
import little_star_function as ls
from settings import Settings


def game_run():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Little Star')

    stars = Group()
    ls.create_fleet(screen, settings.screen_width, settings.screen_height,
                    stars, settings)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ls.update_stars(screen,settings, stars)
        ls.update_screen(screen, settings, stars)


game_run()
