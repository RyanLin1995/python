import asyncio

import aiohttp


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = rf"img/async_{url.rsplit('-')[-2]}.gif"
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)
        print("下载完成", url)


async def main():
    async with aiohttp.ClientSession() as session:
        utl_list = [
            'https://img.nga.178.com/attachments/mon_202306/14/-116cfdQqpt2-2izeXmZ66T3cSgo-8c.gif',
            'https://img.nga.178.com/attachments/mon_202306/14/-116cfdQqpt2-gge2XnZ6bT3cSgo-8c.gif',
            'https://img.nga.178.com/attachments/mon_202306/14/-116cfdQqpt2-9l57XrZ7lT3cSgo-8c.gif'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in utl_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
