def flatten_list(l):
    """
    Returns a list of values, where each element in the returned list is
    a non-list.

    The returned list is a flattened version of l, i.e. removing any
    level of nesting and storing the elements in the order which they appear.

    For example:

    # >>> l = [[["wow"], \
    #     [1, "hello", [1, 2, 100, 999, "weldo"]], \
    #      1, \
    #      2]]
    # >>> flatten_list(l) == ["wow", 1, "hello", 1, 2, 100, 999, "weldo", 1, 2]
    # True
    #
    # >>> l = ["llama", [1, 2, 999, [55, 5]]]
    # >>> flatten_list(l) == ["llama", 1, 2, 999, 55, 5]
    True

    """
    is_flat = True
    for i in range(len(l)):
        if type(l[i]) == list:
            is_flat = False
            return l[0:i] + flatten_list(l[i]) + flatten_list(l[i + 1:len(l)])

    if is_flat:
        return l[:]


# ---------- end provided functions

# --------- add your functions here
l = [[["wow"], [1, "hello", [1, 2, 100, 999, "WELDO"]], 1, 2]]
word = "Weldo"


def check_word_from_list(l, word):
    for char in flatten_list(l):
        if type(char) is str and char.lower() == word.lower():
            word = char
            return word and True
    else:
        return ()


result = check_word_from_list(l, word)

if result:
    for list_index_number in (l):
        print(l.index(list_index_number))