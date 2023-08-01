from collections import namedtuple
from operator import attrgetter

metro_data = [
    ('Tokyo', 'JP', 36.93, (35.68, 139.69)),
    ('Delhi NCR', 'IN', 21.94, (28.61, 77.21)),
    ('Mexico City', 'MX', 20.14, (19.43, -99.13)),
    ('New York-Newark', 'US', 20.1, (40.81, -74.02)),
    ('Sao Paulo', 'BR', 19.65, (-23.55, -46.64))
]
LatLon = namedtuple('LatLon', 'lat lon')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLon(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]
print(metro_areas[0].coord.lat)

# attrgetter 创建的函数会根据名称来提取对象的属性
name_let = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_let(city))
