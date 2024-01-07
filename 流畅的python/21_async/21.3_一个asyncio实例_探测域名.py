import asyncio
import socket
from keyword import kwlist

MAX_KEYWORD_LEN = 4


async def probe(domain: str) -> tuple[str, bool]:
    loop = asyncio.get_running_loop()  # 获取 asyncio 事件循环，供后面使用
    try:
        await loop.getaddrinfo(domain, None)  # 协程 loop.getaddrinfo 返回一个五元组，使用套接字连接指定的地址。如果有结果返回，则说明域名可以解析，否则不可解析
    except socket.gaierror:
        return domain, False

    return domain, True


async def main() -> None:
    names = (kw for kw in kwlist if len(kw) <= MAX_KEYWORD_LEN)
    domains = (f'{name}.dev'.lower() for name in names)
    coros = [probe(domain) for domain in domains]  # 调用 probe 协程，传入各个 domain ，构建一个协程对象列表
    for coro in asyncio.as_completed(coros):  # asyncio.as_completed 是一个生成器，产生协程，按照传入的协程完成的顺序（而不是协程提交的顺序）返回结果
        domain, found = await coro  # 当 asyncio.as_completed 中的某个任务率先执行完毕时，会通过 await 关键字返回该任务的结果
        mark = '+' if found else ' '
        print(f'{mark} {domain}')


if __name__ == '__main__':
    asyncio.run(main())
