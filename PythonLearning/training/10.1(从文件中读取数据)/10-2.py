file_name = 'learning_python.txt'

with open(file_name) as file_object:
    for python in file_object.readlines():
        print(python.replace('Python','Go').strip())
