import csv

with open("example.csv") as f:
    csv_file = csv.reader(f)  # 返回一个 Reader 的对象。不能直接传递文件名给 reader 函数

    for row in csv_file:
        print(f"Row #{csv_file.line_num} {row}")  # line_num 方法返回当前行号。同时 Reader 对象只能遍历一次，遍历完后如果要再操作，需要再调用 Reader 对象