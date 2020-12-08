import json


def input_number():
    """用户输入喜欢的数字"""
    try:
        number = int(input('Please in put your favorite number: '))
    except ValueError:
        print('Please input the number')
    else:
        filename = 'number_1.json'
        with open(filename, 'w') as file_object:
            json.dump(number,file_object)
        return number


def print_number():
    """打印用户喜欢的数字"""
    try:
        filename = 'number_1.json'
        with open(filename) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        number = input_number()
        print('Your favorite is ' + str(number) + '!')
    else:
        print("I know your favorite number! It's " + str(number) + '!')


print_number()
