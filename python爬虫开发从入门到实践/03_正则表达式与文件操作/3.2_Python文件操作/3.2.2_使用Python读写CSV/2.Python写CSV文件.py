import csv

data = [
    {'name': '小明', 'age': 23, 'score': 100},
    {'name': '小芳', 'age': 18, 'score': 88},
    {'name': 'Ryan', 'age': 23, 'score': 100},
]

with open('data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'age', 'score'])
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name': 'Gigi', 'age': 23, 'score': 100})
