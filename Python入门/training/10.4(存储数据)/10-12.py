import json


def get_number():
    """读取数字文件"""
    filename = 'number.json'
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return number


def input_number():
    """用户输入喜欢的数字"""
    try:
        number = int(input('Please in put your favorite number: '))
        filename = 'number.json'
        with open(filename, 'w') as file_object:
            json.dump(number,file_object)
        return number
    except ValueError:
        print('Please input the number!')


def print_number():
    """打印用户喜欢的数字"""
    number = get_number()
    if number:
        print('I will remember your favorite is ' + str(number) + '!')
    else:
        number = input_number()
        print('Your favorite is ' + str(number) + '!')

print_number()
