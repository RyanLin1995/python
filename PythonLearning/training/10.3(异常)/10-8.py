#conding:gbk
def Pet(filename):
    """这是一个打印打多个宠物名字的函数"""
    try:
        with open(filename, 'r') as file_object:
            pet_names = file_object.readlines()
    except FileNotFoundError:
        print('The file: %s not found!' % filename)
    else:
        for pet_name in pet_names:
            print(pet_name.strip())

Pet('cat.txt')

Pet('dog.txt')
