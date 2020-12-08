def city_country(city,country):
    city_name = city + ',' + country
    return city_name.title()

city = city_country('changsha','china')
print(city)

city = city_country('tokyo','japan')
print(city)

city = city_country('lodon','england')
print(city)
