import pygame
import game_function as gf
from settings import Settings
from pygame.sprite import Group
from cow import Cow


def game_run():
    settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode(
        (settings.screen_height, settings.screen_width))
    pygame.display.set_caption('Ball')

    cow = Cow(screen, settings)
    balls = Group()
    gf.create_ball(screen, settings, balls)
    while True:
        gf.check_events(cow)
        if settings.game_limit > 0:
            gf.ball_update(cow, balls, settings, screen)
            cow.update()
        gf.update_screen(screen, settings, cow, balls)


game_run()
