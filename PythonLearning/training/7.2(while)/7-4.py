message = 'Please input the kind of pizza.'
message += "\n(You can input the 'quit' to the end)"

pizza = ''
while pizza != 'quit':
    pizza = input(message)
    print(pizza)
