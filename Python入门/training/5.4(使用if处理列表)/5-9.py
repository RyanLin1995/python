users=[]
if users:
    for user in users:
        if user == 'admin':
            print('Hi' + ' ' + user.title() + ',' + \
        'would you like check the login status?')
        else:
            print('Hello' + ' ' + user.title() + ',' + 'Welcome to PZ')
else:
    print('We need to find some users!')
