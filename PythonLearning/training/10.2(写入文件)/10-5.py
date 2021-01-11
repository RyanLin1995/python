file_name = 'survey.txt'
x = True

while True:
    message = "Why you like to program?"
    print(message)
    reason = input()
    with open(file_name, 'a') as file_object:
        if reason != 'Quit':
            file_object.write(reason + '\n')

        else:
            x = False