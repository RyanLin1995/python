import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'number_3.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    filename = 'number_3.json'
    username = input('Please input your username: ')
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_usr():
    username = get_stored_username()
    if username:
        print('You username is ' + username.title() + ' ,right?')
        print("(If the name isn't yours,please input 'No')")
        confirm = input()
        if confirm.title() == 'No':
            username = get_new_username()
            print('I will remember you,' + username + '!')
        else:
            print('Welcome back ' + username.title() + '!')
    else:
        username = get_new_username()
        print('I will remember you,' + username + '!')


greet_usr()
