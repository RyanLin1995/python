# 使用 bs 的 select 方法并传入一个 CSS 选择器，可以取得 web 页面元素
# CSS 选择器的例子：
# 传递给 select 的选择器                  将匹配的是
# soup.select('div')                    所有名为 <div> 的元素
# soup.select('#author')                带有 id 属性的 author 元素
# soup.select('.notice')                所有使用 CSS class 属性名为 notice 的元素
# soup.select('div span')               所有在 <div> 元素中的 <span> 元素
# soup.select('div > span')             所有直接在 <div> 元素之内的 <span> 元素，中间没有其他元素
# soup.select('input[name]')            所有名为 <input>,并且有一个 name 属性，其值无所谓的元素
# soup.select('input[type="button"]')   所有名为 <input>,并且有一个 type 属性，其值为 button 的元素
# soup.select('p #author')              所有在 <p> 元素内带有 id 属性的 author 元素

import bs4
import requests

# example_file = open("example.html")
example_link = requests.get(url="https://www.baidu.com/s?ie=UTF-8&wd=test")
example_soup = bs4.BeautifulSoup(example_link.text, "html.parser")
elems = example_soup.select('h3 a')  # 返回的是一个 Tag 对象的列表

print(type(elems))  # elems是一个类
print(len(elems))
print(elems)

# print(type(elems[0]))  # 列表中的每一个值都是一个 Tag 对象
# print(elems)
#
# print(elems[0].getText())  # 可以使用Tag 对象的 getText 方法获取该元素的文本
#
# print(elems[0].attrs)  # 可以使用Tag 对象的 attrs 方法获取该元素的属性以及属性的值，在这里属性为 id ，值为 author
#
# print(elems[0].get("id"))  # 可以使用Tag 对象的 get 方法，通过传入属性获得属性的值
