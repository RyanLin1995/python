spam = ['apple', 'bananas', 'tofu', 'cats', 'dogs']


def list_update(list_sorce):

    list_sorce.insert(-1, 'and')

    return ", ".join(list_sorce)


result = list_update(spam)
print(result)