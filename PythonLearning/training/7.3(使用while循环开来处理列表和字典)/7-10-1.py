places = {}
active = True

while active:
    favorite_places= []
    current_number = 0
    print("What's your name?")
    names = str(input())
    while current_number < 3:
        print("Where is your favorite places?")
        place = str(input())
        favorite_places.append(place)
        current_number += 1
        print(favorite_places)
        
    places[names] = favorite_places
    
    print(places)
    
    print('If you want to let other people to respond?(yes/no)')
    respond = input()
    if respond == 'no':
        active = False

for name,favorite_place in places.items():
    print(name.title() + "'s favorite place are:")
    for place in favorite_place:
        print('\n' + place.title())
