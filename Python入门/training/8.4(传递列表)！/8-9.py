def show_magicians(names):
    for name in names:
        message = "Hi" + ' ' + name.title()
        print(message)

names = ['john','ricky','tom']
show_magicians(names)