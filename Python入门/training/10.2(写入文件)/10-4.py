file_name = 'guest_book.txt'
x = True
while x:
    message = 'Please input yor name.'
    message += "\nYou can input 'Quit' to end."
    print(message)
    name = input()
    with open(file_name, 'a') as file_object:
        if name != 'Quit':
            print('Hi %s,Welcome to KN\n'  % name.title())
            file_object.write(name.title() + "\n")
        else:
            x = False