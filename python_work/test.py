def levenshtein_dist(word1, word2, display=False):
    ''' Return the minimum edit distance between two words, word1 and word2.
    The optional display parameter displays the full calculation matrix when
    set to True, and hides it otherwise.

    The minimum edit distance is the minimum number of {swaps, inserts, deletes}
    needed to change word1 to word2 and vice versa.

    levenshtein_dist('capybara', 'llama')
    6
    levenshtein_dist('apple', 'bapple')
    1
    '''

    dist_array = [None] * (len(word1) + 1)
    for i in range(len(word1) + 1):
        dist_array[i] = [0] * (len(word2) + 1)

    for i in range(0, len(word1) + 1):
        for j in range(0, len(word2) + 1):
            if min(i, j) == 0:
                dist_array[i][j] = max(i, j)
            else:
                (val1, val2, val3) = (dist_array[i][j - 1] + 1, dist_array[i - 1][j] + 1, dist_array[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))

                dist_array[i][j] = min(val1, val2, val3)

    if display:
        for item in dist_array:
            print(item)

    return dist_array[-1][-1]


ret = levenshtein_dist("hi", "hello", True)
print(ret)