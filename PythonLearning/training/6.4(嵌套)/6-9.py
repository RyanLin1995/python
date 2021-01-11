favorite_places = {
    'ryan':['tokyo','changsha'],
    'suki':['changsha','los angeles','beihai'],
    'gigi':['shanghai','seoul'],
    }
for name,places in favorite_places.items():
    print(name.title() + "'s favorite place are:")
    for place in places:
        print('\t' + place.title())
