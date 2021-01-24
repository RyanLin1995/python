# WebDriver 对象有好几种方法，用于在页面中寻找元素。它们被分成find_element_*和
# find_elements_*方法。find_element_*方法返回一个 WebElement 对象，代表页面中
# 匹配查询的第一个元素。find_elements_*方法返回 WebElement_*对象的列表，包含
# 页面中所有匹配的元素。
#
# selenium 的 WebDriver 方法，用于寻找元素
# 方法名                                                 返回的 WebElement 对象/列表
# browser.find_element_by_class_name(name)              使用 CSS 类 name 的元素
# browser.find_elements_by_class_name(name)
#
# browser.find_element_by_css_selector(selector)        匹配 CSS selector 的元素
# browser.find_elements_by_css_selector(selector)
#
# browser.find_element_by_id(id)                        匹配 id 属性值的元素
# browser.find_elements_by_id(id)
#
# browser.find_element_by_link_text(text)               完全匹配提供的 text 的<a>元素
# browser.find_elements_by_link_text(text)
#
# browser.find_element_by_partial_link_text(text)       包含提供的 text 的<a>元素
# browser.find_elements_by_partial_link_text(text)
#
# browser.find_element_by_name(name)                    匹配 name 属性值的元素
# browser.find_elements_by_name(name)
#
# browser.find_element_by_tag_name(name)                匹配标签 name 的元素
# browser.find_elements_by_tag_name(name)               (大小写无关，<a>元素匹配'a'和'A')
#
#
# 除了*_by_tag_name()方法，所有方法的参数都是区分大小写的。如果页面上没
# 有元素匹配该方法要查找的元素，selenium 模块就会抛出 NoSuchElement 异常。如
# 果你不希望这个异常让程序崩溃，就在代码中添加 try 和 except 语句。
# 一旦有了 WebElement 对象，就可以其中的属性，或调用其中的方法
#
# WebElement 的属性和方法
# 属性或方法                                描述
# tag_name                                标签名，例如 'a'表示<a>元素
# get_attribute(name)                     该元素 name 属性的值
# text                                    该元素内的文本，例如<span>hello</span>中的'hello'
# clear()                                 对于文本字段或文本区域元素，清除其中输入的文本
# is_displayed()                          如果该元素可见，返回 True，否则返回 False
# is_enabled()                            对于输入元素，如果该元素启用，返回 True，否则返回 False
# is_selected()                           对于复选框或单选框元素，如果该元素被选中，选择 True，否则返回 False
# location                                一个字典，包含键'x'和'y'，表示该元素在页面上的位置


from selenium import webdriver

chrome_drive = r"/home/ryan/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_drive)
browser.get("https://www.baidu.com")

try:
    ret = browser.find_element_by_class_name('title-content-title')
    print(f"Find the {ret.tag_name} element with that class name!")
except:
    print("Fail to find the a element with that class name")

