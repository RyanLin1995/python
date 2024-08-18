from DrissionPage import WebPage, ChromiumOptions

co = ChromiumOptions().use_system_user_path()

page = WebPage(chromium_options=co)
page.get('https://account.guokr.com/sign_in/')
# 等待登录
is_done = str(input("登陆了吗？（登陆了填Done）："))
if is_done.lower() == "done".lower():
    page.wait.url_change(text='https://www.guokr.com/', timeout=10)
    page.change_mode()
    if page.s_ele('text=首页'):
        print('登录成功')
