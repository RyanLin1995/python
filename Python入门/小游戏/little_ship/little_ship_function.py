import pygame
import sys
from little_ship_bullet import Bullet

''''这里存储按键和屏幕等'''


def check_keydown_events(event, settings, screen, little_ship, bullets):
    if event.key == pygame.K_UP:
        little_ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        little_ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, little_ship)
        bullets.add(new_bullet)


def check_keyup_events(event, little_ship):
    if event.key == pygame.K_UP:
        little_ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        little_ship.moving_down = False


def check_event_key(settings, screen, little_ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, little_ship, bullets)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, little_ship)


def update_bullets(bullets, screen):
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.right >= screen_rect.right:
            bullets.remove(bullet)


def update_rect(rect):
    rect.rect_check_edge()
    rect.update()


def update_screen(settings, screen, little_ship, bullets, rect):
    screen.fill(settings.bg)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rect.draw_rect()
    little_ship.blitme()

    pygame.display.flip()