favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
name_lists=['ryan','jen','sarah','edward','gigi','james','phil']

for name in favorite_languages:
    if name in favorite_languages:
        print(name.title() + ',' + 'Thanks for your provide!')
for name_list in name_lists:
    if name_list not in favorite_languages.keys():
        print(name_list.title() + ',' + 'Could you kindly provide your info?')
print('\n')        
for name in sorted(name_lists):
    if name in favorite_languages:
        print(name.title() + ',' + 'Thanks for your provide!')
    else:
        print(name.title() + ',' + 'Could you kindly provide your info?')
