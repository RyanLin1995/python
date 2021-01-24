from selenium import webdriver

chrome_drive = r"/home/ryan/Downloads/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_drive)
print(type(browser))

browser.get("https://www.baidu.com")