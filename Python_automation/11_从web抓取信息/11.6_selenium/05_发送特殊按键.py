import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_drive = r"/home/ryan/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_drive)
browser.get(r"https://www.baidu.com")
kw = browser.find_element_by_id('kw')
kw.send_keys('test')
su = browser.find_element_by_id('su')
su.submit()
time.sleep(1)
html = browser.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(0.5)
html.send_keys(Keys.HOME)
