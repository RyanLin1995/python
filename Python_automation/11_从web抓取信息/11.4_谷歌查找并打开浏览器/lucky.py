import webbrowser
import requests
import bs4

# Get the search word
print('Input the keyword:')
word = input()
print('Gooling.......')
res = requests.get("http://www.baidu.com/s?ie=UTF-8&wd={}".format(word))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
link_elems = soup.select('.t a')
open_num = min(5, len(link_elems))
for i in range(open_num):
    webbrowser.open(link_elems[i].get("href"))


