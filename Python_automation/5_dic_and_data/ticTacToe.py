theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-m': ' ', 'low-R': ' '}


def printBoard(board):
    print("{}|{}|{}".format(board['top-L'], board['top-M'], board['top-R']))
    print('-+-+-')
    print("{}|{}|{}".format(board['mid-L'], board['mid-M'], board['mid-R']))
    print('-+-+-')
    print("{}|{}|{}".format(board['low-L'], board['low-m'], board['low-R']))


if __name__ == '__main__':
    trun = "X"
    for i in range(9):
        printBoard(theBoard)
        print("Trun for {}, move on which space?".format(trun))
        move = input()
        theBoard[move] = trun
        if trun == "X":
            trun = "O"
        else:
            trun = "X"
    printBoard(theBoard)