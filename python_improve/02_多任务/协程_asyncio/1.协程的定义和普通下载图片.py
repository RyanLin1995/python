# 协程就是一个线程中遇到IO等待的时候不会一直等待，而是会执行其他任务
import requests


def download_image(url):
    print("开始下载：", url)
    # 发送网络请求，下载图片
    response = requests.get(url)
    print("下载完成")
    # 图片保存到本地文件
    file_name = rf"img/{url.rsplit('-')[-1]}"
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    utl_list = [
        'https://w.wallhaven.cc/full/x6/wallhaven-x6pl9v.jpg',
        'https://w.wallhaven.cc/full/we/wallhaven-we628p.jpg',
        'https://w.wallhaven.cc/full/48/wallhaven-48opm1.jpg'
    ]
    for item in utl_list:
        download_image(item)
