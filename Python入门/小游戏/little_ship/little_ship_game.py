import pygame
import little_ship_function as function
from little_ship_setting import Setting
from little_ship_ship import Little_ship
from pygame.sprite import Group
from rect import Rect


'''这是一个小飞船的游戏'''


def game_run():
    pygame.init()
    settings = Setting()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption('little ship')

    little_ship = Little_ship(settings, screen)
    bullets = Group()
    rect = Rect(screen, settings)

    while True:
        function.check_event_key(settings, screen, little_ship, bullets)
        little_ship.little_ship_update()
        function.update_bullets(bullets, screen)
        function.update_rect(rect)
        function.update_screen(settings, screen, little_ship, bullets, rect)


game_run()
