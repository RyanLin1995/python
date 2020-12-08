allGuests = {'Alice': {'apple': 5, 'pretzels': 12},
             'Bob': {'ham sandwiched': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print("Number of things being brought")
print("-Apples  {}".format(str(totalBrought(allGuests, 'apple'))))
print("-ham sandwiched  {}".format(str(totalBrought(allGuests, 'ham sandwiched'))))
print("-Oranges {}".format(str(totalBrought(allGuests, 'oranges'))))
print("-pretzels {}".format(str(totalBrought(allGuests, 'pretzels'))))