import requests
import bs4

# 通过request读取网页数据后，返回给BeautifulSoup对象
res = requests.get(r"https://www.baidu.com")
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"html.parser")  # html.parser 为解析器
print(type(noStarchSoup))

# 读取本地HTML文件返回给BeautifulSoup对象
example_file = open("example.html")
example_soup = bs4.BeautifulSoup(example_file, "html.parser")
print(type(example_soup))