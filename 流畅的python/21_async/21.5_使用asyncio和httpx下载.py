#!/usr/bin/env python3

"""Download flags of top 20 countries by population

asyncio + aiottp version

Sample run::

    $ python3 flags_asyncio.py
    EG VN IN TR RU ID US DE CN MX JP BD NG ET FR BR PH PK CD IR
    20 flags downloaded in 1.07s
"""
# tag::FLAGS_ASYNCIO_TOP[]
import asyncio

from httpx import AsyncClient

from flags import BASE_URL, save_flag, main


async def download_one(client: AsyncClient, cc: str):  # 重写函数以符合协程
    image = await get_flag(client, cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


async def get_flag(client: AsyncClient, cc: str) -> bytes:  # 利用 httpx 重写函数以符合协程。需要接收发起请求的 AsyncClient
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                            follow_redirects=True)  # 返回的是一个 ClientResponse 对象，是一个异步管理器
    return resp.read()  # 获取返回信息


# end::FLAGS_ASYNCIO_TOP[]

# tag::FLAGS_ASYNCIO_START[]
def download_many(cc_list: list[str]) -> int:  # 这是一个常规函数，作为协程的调用口，以供 main 调用
    return asyncio.run(
        supervisor(cc_list))  # 执行事件循环，驱动 supervisor 协程对象，直到协程返回。在事件循环运行期间，这行代码一直阻塞。返回的结果是 supervisor 返回的内容


async def supervisor(cc_list: list[str]) -> int:
    async with AsyncClient() as client:  # AsyncClient方法是 httpx 中异步的客户端
        to_do = [download_one(client, cc)
                 for cc in sorted(cc_list)]  # 每下载一次国旗就调用一次 download_one 协程，构建一个协程列表
        res = await asyncio.gather(*to_do)  # asyncio.gather 接受的参数是一个或多个可异步调用对象，等全部执行完毕，以可异步调用对象的提交顺序返回结果列表

    return len(res)  # supervisor 返回 asyncio.gather 返回的列表长度


if __name__ == '__main__':
    main(download_many)
# end::FLAGS_ASYNCIO_START[]
