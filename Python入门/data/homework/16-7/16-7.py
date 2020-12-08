import csv
import pygal
from pygal_maps_world.i18n import COUNTRIES

file = 'API_SP.POP.2529.FE.5Y_DS2_en_csv_v2_1139511.csv'


def get_country_code(country):
    for code, name in COUNTRIES.items():
        if country == name:
            return code
    else:
        return None


data_value = {}
with open(file, encoding='utf8') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        code = get_country_code(row[0])
        try:
            row_4_value = '{:.2}'.format(float(row[4]))
        except ValueError:
            continue
        print(row_4_value)
        if code:
            data_value[code] = float(row_4_value)

print(data_value)

wm = pygal.maps.world.World()
wm.add('1960', data_value)
wm.render_to_file('1960.svg')
