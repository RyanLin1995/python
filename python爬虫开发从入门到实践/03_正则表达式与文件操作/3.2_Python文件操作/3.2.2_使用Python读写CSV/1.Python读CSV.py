import csv

with open('result.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        username = row['username']
        content = row['content']
        reply_time = row['reply_time']
        print("用户名：{}，回复内容：{}".format(username, content))
