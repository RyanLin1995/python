def describe_city(city_name,country = 'china'):
    print(city_name.title() + ' ' + 'is belong to' + ' ' + country.title() + 
    '.')

describe_city('changsha')
describe_city(city_name = 'chongqing')
describe_city('Tokyo','Japan')

