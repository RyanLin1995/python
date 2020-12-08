from rain import Rain
from pygame.sprite import Sprite


def get_number_rain_x(screen_width, rain_width):
    available_space_x = screen_width - 2 * rain_width
    number_rain_x = int(available_space_x / (2 * rain_width))
    return number_rain_x


def get_number_rain_y(screen_height, rain_height):
    available_space_y = screen_height - 2 * rain_height
    number_rain_y = int(available_space_y / (2 * rain_height))
    return number_rain_y


def create_rain(screen, rains, rain_list_numger, rain_row_number):
    rain = Rain(screen)
    rain_width = rain.rect.width
    rain_height = rain.rect.height
    rain.x = rain_width + 2 * rain_width * rain_row_number
    rain.y = rain_height + 2 * rain_height * rain_list_numger
    rain.rect.x = rain.x
    rain.rect.y = rain.y
    rains.add(rain)


def create_rains(screen, screen_width, screen_height, rains):
    rain = Rain(screen)
    number_rain_x = get_number_rain_x(screen_width, rain.rect.width)
    number_rain_y = get_number_rain_y(screen_height, rain.rect.height)
    for rain_y in range(number_rain_y):
        for rain_x in range(number_rain_x):
            create_rain(screen, rains, rain_y, rain_x)


def check_rains_edges(screen, rains):
    for rain in rains.sprites():
        if rain.check_edge():
            new_rain = Rain(screen)
            new_rain.rect.x = rain.rect.x
            rains.remove(rain)
            rains.add(new_rain)
        print(rains)


def update_rains(screen, rains):
    check_rains_edges(screen, rains)
    rains.update()