import asyncio

from aiohttp import request
from aiomultiprocess import Pool


async def get(url):
    async with request("GET", url) as response:
        return await response.json()


async def main():
    urls = ["http://date.jsontest.com/", "http://headers.jsontest.com/", "http://ip.jsontest.com/"]
    async with Pool() as pool:
        async for result in pool.map(get, urls):
            # 处理下载的文件数据
            print(result)


if __name__ == '__main__':
    # Python 3.7及以上版本
    asyncio.run(main())

    # Python 3.6版本
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
