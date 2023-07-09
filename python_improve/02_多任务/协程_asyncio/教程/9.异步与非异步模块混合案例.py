import asyncio
import time

import requests


async def download_picture(url):
    # 发送网络请求，下载图片【遇到网络下载图片的 IO 请求，自动化切换到其他任务】
    print("开始下载", url)

    loop = asyncio.get_event_loop()
    # requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print("下载完成")
    file_name = rf"img/async_{url.rsplit('-')[-2]}.gif"
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    start = time.time()
    utl_list = [
        'https://img.nga.178.com/attachments/mon_202306/14/-116cfdQqpt2-2izeXmZ66T3cSgo-8c.gif',
        'https://img.nga.178.com/attachments/mon_202306/14/-116cfdQqpt2-gge2XnZ6bT3cSgo-8c.gif',
        'https://img.nga.178.com/attachments/mon_202306/14/-116cfdQqpt2-9l57XrZ7lT3cSgo-8c.gif'
    ]

    tasks = [download_picture(url) for url in utl_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print(end - start)
