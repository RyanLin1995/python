import json
from pygal_maps_world.i18n import COUNTRIES

file = 'population_data.json'
with open(file) as f:
    pop_data = json.load(f)

country_name = []
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':
        country_name.append(pop_dict['Country Name'])

country_code = []
miss_country_code = []
for c_name in country_name:
    for code, name in COUNTRIES.items():
        if c_name == name:
            country_code.append(code)
            break
    else:
        miss_country_code.append(c_name)


print((COUNTRIES))
print((miss_country_code))
print(len(country_code))





