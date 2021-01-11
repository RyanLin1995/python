file_name = 'learning_python.txt'

with open(file_name) as file_object_1:
    python = file_object_1.read()
    print(python + '\n')

with open(file_name) as file_object_2:
    for line_2 in file_object_2.readlines():
        print(line_2.rstrip())

with open(file_name) as file_object_3:
    lines_3 = file_object_3.readlines()

line = []
for line_3 in lines_3:
    line.append(line_3.strip())
print('\n' + str(line))
