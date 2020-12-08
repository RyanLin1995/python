def collatz(number):
    """Collatz"""
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


try:
    num = int(input('Please input the number: '))

    while True:
        if num != 1:
            num = collatz(num)
        else:
            break

except ValueError:
    print('Please input a number')




