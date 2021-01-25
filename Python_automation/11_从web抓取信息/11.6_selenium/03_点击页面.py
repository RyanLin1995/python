from selenium import webdriver

chrome_drive = r"/home/ryan/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_drive)
browser.get("https://www.baidu.com")
link_elem = browser.find_element_by_link_text('新闻')
print(type(link_elem))
link_elem.click()