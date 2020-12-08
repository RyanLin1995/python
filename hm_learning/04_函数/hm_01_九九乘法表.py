def multiple_table():
    row = 1

    while row <= 9:
        col = 1
        while col <= row:
            print(str(col) + '*' + str(row) + '=' + str(col*row), end=' ')
            col += 1

        print('')

        row += 1