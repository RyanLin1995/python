import requests

res = requests.get(url='http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

print(res.status_code)

print(len(res.text))
