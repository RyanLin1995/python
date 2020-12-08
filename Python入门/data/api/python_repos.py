import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS

# 执行API调用并存储响应
uel = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(uel)
print("Status code: {}".format(r.status_code))

# 将API响应存储在一个变量中
response_dict = r.json()
print('Total repositories: {}'.format(response_dict['total_count']))

# 探索有关仓库的信息
repo_dicts = response_dict['items']
# print('Repositories returned: {}'.format(len(repo_dicts)))
#
# print("\nSelected information about first repository:")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

my_style = LS(base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.style.title_font_size = 24
my_config.style.label_font_size = 14
my_config.style.major_label_font_size = 20
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
<<<<<<< HEAD
#chart.render_in_browser()
=======
# chart.render_in_browser()
>>>>>>> da53f134afe2457bcd8bacd6a706d877ac6f6b74



