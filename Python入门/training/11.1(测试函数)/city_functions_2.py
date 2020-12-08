def city_info_2(city, country, population = ''):
    if population:
        cityinfo_2 = city.title() + ', ' + country.title() + \
               ' -population ' + str(population)
    else:
        cityinfo_2 = city.title() + ', ' + country.title()

    return cityinfo_2


