l = [[["wow"], [1, "hello", [1, 2, 100, 999, "WELDO"]], 1, 2]]
word = "Weldo"


def flatten_list(l):
    is_flat = True
    for i in range(len(l)):
        if type(l[i]) == list:
            is_flat = False
            return l[0:i] + flatten_list(l[i]) + flatten_list(l[i + 1:len(l)])

    if is_flat:
        return l[:]


def check_word_from_list(l, word):
    global index_number
    for char in flatten_list(l):
        if type(char) is str and char.lower() == word.lower():
            word = char
            return word and True
    else:
        return ()


result = flatten_list(l)
print(result)