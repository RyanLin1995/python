def make_great(greats):
    for i in range(0,len(greats)):
        greats[i] = 'the great' + ' ' + greats[i]
        print(greats)

def show_magicians(names):
    for name in names:
        message = "Hi" + ' ' + name.title()
        print(message)

greats = ['john', 'ricky', 'tom']
make_great(greats)
show_magicians(greats)
