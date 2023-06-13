import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX')
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City('Asia', _, country):  # 位置参数由__match_args__特殊类属性实现
                results.append(country)
    return results


print(match_asian_cities())
