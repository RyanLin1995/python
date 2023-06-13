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
            case City(continent='Asia', country=country):  # country=country 意味着将变量 country 绑定到实例的 country 属性上
                results.append(country)
    return results


print(match_asian_cities())
