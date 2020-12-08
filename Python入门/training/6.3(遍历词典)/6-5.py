rivers={
    'nile':'egypt',
    'amazon':'brazil',
    'yangtze':'china',
    }
for name,country in rivers.items():
    print('The' + ' ' + name.title() + ' ' + 'runs through' + ' ' + 
    country.title())

print('\n')    
for name in rivers:
    print(name.title())

print('\n')    
for name in rivers.keys():
    print(name.title())

print('\n')    
for country in rivers.values():
    print(country.title())
