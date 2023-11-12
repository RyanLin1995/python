import fileinput

with fileinput.input(files=('test1.txt', 'test2.txt'), inplace=True) as f:
    for line in f:
        # print(f.filename(), line)  # 注意，每一个 print 都是对每一行的修改
        print(line.strip() + '->我是回写')
