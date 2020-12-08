places = {}

active = True

while active:
    print("What's your name?")
    names = str(input())
    
    print("Where is your favorite places?")
    place = str(input())
    
    places[names] = place
    
    print('If you want to let other people to respond?(yes/no)')
    respond = str(input())
    if respond == 'no':
        active = False

for name,favorite_place in places.items():
    print(name.title() + "'s favorite place is:" + ' ' + 
    favorite_place.title())
    
