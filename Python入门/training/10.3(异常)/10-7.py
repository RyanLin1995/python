'''一个循环的加法运算错误的例子'''
x = True

while x:
    try:
        print('Please input the First number: ')
        num_1 = int(input())
        print('Please input Second number: ')
        num_2 = int(input())
        result = num_1 + num_2
        print('The result is %d.' % result)
    except ValueError:
        print('Please input the number')