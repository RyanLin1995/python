cities = {
    'beijing':{
        'country':'china',
        'population':1000000,
        'sign':'the palace museun',
        },
        
    'shanghai':{
        'country':'china',
        'population':1500000,
        'sign':'qriental pearl',
        },
        
    'guangzhou':{
        'country':'china',
        'population':1200000,
        'sign':'canton tower',
        }
    }
for city,cities_info in cities.items():
    print('\n' + city.title() + "'s info are:")
    print('It is belongs to' + ' ' + cities_info['country'].title())
    print('It has' + ' ' + str(cities_info['population']) + ' ' + 'people.')
    print('It has' + ' ' + cities_info['sign'].title() + '.')
