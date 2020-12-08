import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print('英雄的原点 {} {}'.format(hero_rect.x, hero_rect.y))
print('英雄的尺寸 {} {}'.format(hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
print('{} {}'.format(hero_rect.size[0], hero_rect.size[1]))