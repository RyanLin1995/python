def make_great(greats,names):
    while greats:
        current_name = greats.pop()
        names.append('the great' + ' ' + current_name)

def show_magicians(names):
    for name in names:
        message = "Hi" + ' ' + name.title()
        print(message)

greats = ['john','ricky','tom']
names = []
make_great(greats,names)
show_magicians(names)