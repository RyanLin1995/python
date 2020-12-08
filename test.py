message = "The default handling of DeprecationWarning has been changed such that these warnings are once more shown by default, but only when the code triggering them is running directly in the __main__ module. As a result, developers of single file scripts and those using Python interactively should once again start seeing deprecation warnings for the APIs they use, but deprecation warnings triggered by imported application, library and framework modules will continue to be hidden by default."


def count_word(messages):
    count = {}

    for character in messages:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    return count


def get_count_word(item, value):

    return item.get(value, 0)


count_result = count_word(message)
get_result = get_count_word(count_result, "x")
print(count_result)
print(get_result)