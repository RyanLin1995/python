pizzas=["9inches" , "10inches" , "12inches"]
friend_pizzas=pizzas[:]
pizzas.insert(0,"7inches")
friend_pizzas.append("15inches")

print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)


print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

