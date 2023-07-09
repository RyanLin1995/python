import asyncio

import aiohttp


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text()
        print("得到结果：", url, len(text))
        return text


async def main():
    async with aiohttp.ClientSession() as session:
        utl_list = [
            'https://www.baidu.com',
            'https://www.qq.com',
            'https://www.163.com'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in utl_list]
        done, pending = await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
