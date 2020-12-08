import sys
import pygame
import time
from ball import Ball
from random import randint


def create_ball(screen, settings, balls):
    ball = Ball(screen, settings)
    balls.add(ball)


def check_keydown_events(event, cow):
    if event.key == pygame.K_RIGHT:
        cow.moving_right = True
    elif event.key == pygame.K_LEFT:
        cow.moving_letf = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, cow):
    if event.key == pygame.K_RIGHT:
        cow.moving_right = False
    elif event.key == pygame.K_LEFT:
        cow.moving_letf = False


def check_events(cow):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, cow)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, cow)


def check_ball_bottom(screen, balls, cow, settings):
    screen_rect = screen.get_rect()
    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            settings.game_limit -= 1
            balls.empty()
            create_ball(screen, settings, balls)
            cow.center_cow()
            time.sleep(0.5)


def ball_update(cow, balls, settings, screen):
    balls.update()
    if pygame.sprite.spritecollideany(cow, balls):
        balls.empty()
        create_ball(screen, settings, balls)
        cow.center_cow()
        time.sleep(0.5)

    check_ball_bottom(screen, balls, cow, settings)


def update_screen(screen, settings, cow, balls):
    screen.fill(settings.bg_color)
    balls.draw(screen)
    cow.blitme()

    pygame.display.flip()
