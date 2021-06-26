import csv

# 普通 csv 写入方式
with open("new.csv", "w", newline="") as f:  # windows 中需要传入 newline="" 参数防止出现两倍行距
    csv_file = csv.writer(f)
    csv_file.writerow(['spam', 'eggs', 'bacon', 'ham'])
    csv_file.writerow(['Hello, World!', 'eggs', 'bacon', 'ham'])
    csv_file.writerow([1, 2, 3.14152, 4])

# 两倍行距和制表符分隔
with open("new.tsv", "w", newline="") as nf:
    new_csv_file = csv.writer(nf, delimiter='\t', lineterminator='\n\n')
    new_csv_file.writerow(['apple', 'oranges', 'grapes'])
    new_csv_file.writerow(['eggs', 'bacon', 'ham'])
    new_csv_file.writerow(['spam', 'spam', 'spam', 'spam', 'spam'])
