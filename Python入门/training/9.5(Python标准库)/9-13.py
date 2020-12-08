from collections import OrderedDict

python = OrderedDict()

python['pop'] = 'The element is popup and available'
python['sort'] = 'Permanently sorted list'
python['sorted'] = 'Temporarily sorted list'
python['len'] = 'Calculate list length'
python['strip'] = 'Delete the blank'
python['key'] = 'key'
python['value'] = 'value'
python['if'] = 'condition'
python['rstrip'] = 'Delete the right blank'
python['lstrip'] = 'Delete the left blank'

for word,mean in python.items():
    print(word.title() + ' ' + 'means' + ':' + mean.title())