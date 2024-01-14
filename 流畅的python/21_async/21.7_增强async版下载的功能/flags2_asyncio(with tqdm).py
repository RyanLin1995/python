#!/usr/bin/env python3

"""Download flags of countries (with error handling).

asyncio async/await version

"""
# tag::FLAGS2_ASYNCIO_TOP[]
import asyncio
from collections import Counter
from http import HTTPStatus
from pathlib import Path
from typing import Optional

import httpx
import tqdm  # type: ignore

from flags2_common import main, DownloadStatus, save_flag

# 较少的默认并发数,防止远程网页503错误
# such as 503 - Service Temporarily Unavailable
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000


async def get_flag(client: httpx.AsyncClient,  # 新增 client 参数
                   base_url: str,
                   cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=3.1, follow_redirects=True)  # client.get 是 httpx.AsyncClient 的方法，所以需要 await
    resp.raise_for_status()
    return resp.content


async def download_one(client: httpx.AsyncClient,
                       cc: str,
                       base_url: str,
                       semaphore: asyncio.Semaphore,
                       verbose: bool) -> DownloadStatus:
    try:
        async with semaphore:  # 信号量。将 semaphore 作为上下文管理器使用，防止整个程序出现阻塞。当信号量计数器为零时，只有这个协程终止运行
            image = await get_flag(client, base_url, cc)
    except httpx.HTTPStatusError as exc:  # 错误处理
        res = exc.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise
    else:
        await asyncio.to_thread(save_flag, image, f'{cc}.gif')  # 将文件 I/O 操作丢给线程运行，防止事件循环阻塞
        status = DownloadStatus.OK
        msg = 'OK'
    if verbose and msg:
        print(cc, msg)
    return status


# end::FLAGS2_ASYNCIO_TOP[]

# tag::FLAGS2_ASYNCIO_START[]
async def supervisor(cc_list: list[str],
                     base_url: str,
                     verbose: bool,
                     concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    semaphore = asyncio.Semaphore(concur_req)  # 创建 asyncio.Semaphore 实例，即为信号表。不允许接收了信号表的活动协程数量超过 concur_req
    async with httpx.AsyncClient() as client:
        to_do = [download_one(client, cc, base_url, semaphore, verbose)
                 for cc in sorted(cc_list)]  # 创建协程对象列表，一个元素对应一次 download_one 协程调用
        to_do_iter = asyncio.as_completed(to_do)  # 获取一个迭代器，返回处理完毕的协程对象
        if not verbose:
            to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))  # 使用 tqdm 生成器函数包装 as_completed 迭代器以显示进度
        error: Optional[
            httpx.HTTPError] = None  # 声明一个 error，默认为 None。用于存储 try/except 抛出的异常。因为把 except 异常绑定到变量上，其作用域只是该 except 异常中
        for coro in to_do_iter:  # 迭代已完成的协程对象
            try:
                status = await coro  # 获取结果。这一步不阻塞，因为 as_complete 只产生已完成的协程
            except httpx.HTTPStatusError as exc:
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exc.response)
                error = exc  # 将错误信息赋值给error。因为 exc 的作用域只在这个 except 下，所以必须赋值给一个该作用域外的值
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
                error = exc
            except KeyboardInterrupt:
                break

            if error:
                status = DownloadStatus.ERROR  # 如有错误，设置status
                if verbose:
                    url = str(error.request.url)  # 从抛出的异常中提取 url
                    cc = Path(url).stem.upper()  # 再提取文件名称
                    print(f'{cc} error: {error_msg}')  # 显示国家代码
            counter[status] += 1

    return counter


def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int) -> Counter[DownloadStatus]:
    coro = supervisor(cc_list, base_url, verbose, concur_req)
    counts = asyncio.run(coro)  # download_many 实例化 supervisor 协程对象，通过 asyncio.run 传给事件循环，在事件循环结束后获得 supervisor 返回的计数器

    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
# end::FLAGS2_ASYNCIO_START[]
