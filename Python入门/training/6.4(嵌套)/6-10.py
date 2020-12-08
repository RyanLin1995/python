favorite_numb={
    'ryan':[18,15,27],
    'jerry':[32,66,45,58],
    'jay':[20,30],
    'nana':[15],
    'gigi':[23]
    }
for name,numbs in favorite_numb.items():
    if len(numbs) > 1:
        print(name.title() + "'s favorite numbers are:")
        for numb in numbs:
            print(str(numb))
    else:
        print(name.title() + "'s favorite numbers is:" + '\n' + str(numbs[0]))


