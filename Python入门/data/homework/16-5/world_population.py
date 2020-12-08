import json
import pygal
from country_code import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

# 将数据加载到一个列表
file = "population_data.json"
with open(file) as f:
    pop_data = json.load(f)

cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pop_1, cc_pop_2, cc_pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop

print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm_style = RotateStyle('#774455', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.titles = "World Population in 2010, by Country"
wm.add('0-10m', cc_pop_1)
wm.add('10m-1bn', cc_pop_2)
wm.add('>1bn', cc_pop_3)


wm.render_to_file('world_population.svg')


