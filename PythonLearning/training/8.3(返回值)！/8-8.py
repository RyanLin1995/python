#coding:gbk
def make_album(singer,album,year=''):
    cd_name = {'name':singer,'cd':album}
    if year:
        cd_name['year'] = year
    return cd_name
    
while True:
    print('\nPlease input the singer name')
    print("\You can input 'q' to quit any time")
    
    name = str(input('Singer:'))
    if name == 'q':
        break
    
    cd = str(input('CD:'))
    if cd == 'q':
        break

    years = input('Years:')
    if years == 'q':
        break
        
    result = make_album(name,cd,years)
    print(result)
