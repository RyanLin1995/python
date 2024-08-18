import requests
import lxml.html

# 获取用户名跟密码
username = str(input("请输入用户名："))
pwd = str(input("请输入密码："))

url = 'https://account.guokr.com/sign_in/'
captcha_url = "https://account.guokr.com/captcha/{}"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}

session = requests.Session()  # 这个是重点，不然的话，每次下载的验证码都是不同的
html = session.get(url, headers=header).content.decode()


def get_login_info():
    selector = lxml.html.fromstring(html)
    token = selector.xpath('//input[@id="csrf_token"]/@value')[0]
    captcha_rand = selector.xpath('//input[@id="captchaRand"]/@value')[0]
    with open('guokr.png', 'wb') as f:
        f.write(requests.get(captcha_url.format(captcha_rand)).content)
    captcha_str = str(input("请输入验证码："))

    # 请求登录
    data_guokr = {
        'csrf_token': token,
        'username': username,
        'password': pwd,
        'captcha': captcha_str,
        'captcha_rand': captcha_rand,
        'permanent': 'y'
    }
    return data_guokr


def get_user_profile():
    request_data = get_login_info()
    r = session.post(url, data=request_data, headers=header)
    if r.status_code == 200:
        print(r.content)


if __name__ == '__main__':
    get_user_profile()
