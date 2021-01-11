def count_words(filename):
    '''这是一个分析一个文本有多少字的函数'''
    try:
        with open(filename,'r') as file_object:
            words = file_object.read()
    except FileNotFoundError:
        print('The file: %s not found!' % filename)
    else:
        words_split = words.split()
        print(len(words_split))
        words_count = words_split.count('the')
        print(words_count)

count_words('Peter Pan by J. M. Barrie.txt')