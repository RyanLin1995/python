import asyncio
import socket
from collections.abc import Iterable, AsyncIterator
from typing import NamedTuple, Optional


class Result(NamedTuple):  # 使用 NamedTuple，probe 的结果更易于阅读和调试。
    domain: str
    found: bool


OptionalLoop = Optional[asyncio.AbstractEventLoop]  # 这个类型别名是为了防止下一行太长，超出打印范围


async def probe(domain: str,
                loop: OptionalLoop = None) -> Result:  # probe 现在接受一个可选的 loop 参数，免得在 multi_probe 驱动这个协程的过程中不断调用 get running_loop。
    if loop is None:
        loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(domain, None)
    except socket.gaierror:
        return Result(domain, False)
    return Result(domain, True)


async def multi_probe(domains: Iterable[str]) -> AsyncIterator[
    Result]:  # 异步生成器函数产生一个异步生成器对象，可以注解为 AsyncIterator[SomeType]
    loop = asyncio.get_running_loop()
    coros = [probe(domain, loop) for domain in domains]  # 构建一个 probe 协程对象列表，对应各个域名
    for coro in asyncio.as_completed(coros):  # 不能使用 async for，因为 asyncio.as_completed 是传统生成器
        result = await coro  # 异步等待协程对象，获取结果
        yield result  # 产出result。有这一行的存在，multi_probe 才是异步生成器
