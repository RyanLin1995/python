import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import Gamestats
from pygame.sprite import Group
from button import Button
from Scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    ai_settings = Settings()
    pygame.init()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption('Ailen Invasion')

    button = Button(ai_settings, screen, 'Play')
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监控键盘和鼠标事件
        gf.check_events(ship, ai_settings, screen, bullets, stats, button, aliens, sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(stats, aliens, bullets, ai_settings, screen, ship, sb)

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, button, stats, sb)


run_game()
