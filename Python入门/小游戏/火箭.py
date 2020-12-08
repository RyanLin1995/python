import pygame
import sys

'''这是一个火箭的小游戏'''
# 小火箭
class Rocket():
    def __init__(self, rocket_screen):
        self.rocket_screen = rocket_screen
        self.speed = 3.5

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rest = self.rocket_screen.get_rect()

        self.rect.centerx = self.screen_rest.centerx
        self.rect.centery = self.screen_rest.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

    def rocket_update(self):
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.speed
        if self.moving_right and self.rect.right < self.screen_rest.right:
            self.centerx += self.speed

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rest.bottom:
            self.centery += self.speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        self.rocket_screen.blit(self.image, self.rect)


def check_keydown_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True

    print(event)

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = False

# 主程序
def run_game():
    # 初始化游戏并创建一个游戏屏幕
    bg_color = (255, 255, 255)
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('小火箭')

    ship= Rocket(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

        ship.rocket_update()

        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()

