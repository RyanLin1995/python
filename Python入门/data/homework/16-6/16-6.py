import json
import pygal
from matplotlib import pyplot as plt
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country):
    for code, name in COUNTRIES.items():
        if country == name:
            return code
    else:
        return None


file = "gdp.json"
with open(file) as f:
    gdp_data = json.load(f)
gpd_value = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2014:
        country = gdp_dict['Country Name']
        value = int(float(gdp_dict['Value']))
        value_update = int(float('{:20}'.format(value/1000000000)))
        code = get_country_code(country)
        if code:
            gpd_value[code] = value_update
print(gpd_value)
wm = pygal.maps.world.World()
wm.titles = "The World GDP in 2014"
wm.add('2014', gpd_value)
wm.render_to_file("gdp.svg")
# gpd_value_key = []
# gpd_value_value = []
# for key, value in gpd_value.items():
#     gpd_value_key.append(key)
#     gpd_value_value.append(value)
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(gpd_value_key, gpd_value_value)
# plt.tick_params(axis='both')
# plt.show()
