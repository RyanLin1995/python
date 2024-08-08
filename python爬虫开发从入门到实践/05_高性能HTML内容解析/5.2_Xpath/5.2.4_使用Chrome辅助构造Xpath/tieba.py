import requests
import lxml.html

content = requests.get('https://tieba.baidu.com/f?kw=%E5%8E%9F%E7%A5%9E%E5%86%85%E9%AC%BC').content
selector = lxml.html.fromstring(content)
title_list = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/text()')
for title in title_list:
    print(title)
