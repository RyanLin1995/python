from little_star import Star
import pygame


def get_number_star_x(screen_width, star_width):
    available_space_x = screen_width - 2 * star_width
    number_star_x = int(available_space_x / (2 * star_width))
    return number_star_x


def get_number_star_y(screen_height, star_height):
    available_space_y = screen_height - 2 * star_height
    number_star_y = int(available_space_y / (2 * star_height))
    return number_star_y


def create_star(screen, stars, star_number, star_row, settings):
    star = Star(screen, settings)
    star_width = star.rect.width
    star_height = star.rect.height
    star.x = star_width + 2 * star_width * star_number
    star.y = star_height + 2 * star_height * star_row
    star.rect.x = star.x
    star.rect.y = star.y
    stars.add(star)


def create_fleet(screen, screen_width, screen_height, stars, settings):
    star = Star(screen, settings)
    number_star_x = get_number_star_x(screen_width, star.rect.width)
    number_star_y = get_number_star_y(screen_height, star.rect.height)
    for star_y in range(number_star_y):
        for star_x in range(number_star_x):
            create_star(screen, stars, star_x, star_y, settings)


# def check_fleet_direction(screen,settings, stars):
#     for star in stars.sprites():
#         new_star = Star(screen, settings)
#         new_star.rect.x = star.rect.x
#         stars.remove(star)
#         stars.add(new_star)


def check_fleet_edges(screen,settings, stars):
    for star in stars.sprites():
        if star.check_edge():
            # check_fleet_direction(screen,settings, stars)
            new_star = Star(screen, settings)
            new_star.rect.x = star.rect.x
            stars.remove(star)
            stars.add(new_star)


def update_stars(screen,settings, stars):
    check_fleet_edges(screen,settings, stars)
    stars.update()


def update_screen(screen, settings, stars):
    screen.fill(settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()

