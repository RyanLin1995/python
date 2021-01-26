from selenium import webdriver

chrome_drive = r"/home/ryan/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_drive)
browser.get("https://www.baidu.com")
kw = browser.find_element_by_id('kw')
kw.send_keys("test")
su = browser.find_element_by_id('su')
su.submit()
