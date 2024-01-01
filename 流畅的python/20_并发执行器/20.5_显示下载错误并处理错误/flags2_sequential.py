#!/usr/bin/env python3

"""Download flags of countries (with error handling).

Sequential version

Sample run::

    $ python3 flags2_sequential.py -s DELAY b
    DELAY site: http://localhost:8002/flags
    Searching for 26 flags: from BA to BZ
    1 concurrent connection will be used.
    --------------------
    17 flags downloaded.
    9 not found.
    Elapsed time: 13.36s

"""

# tag::FLAGS2_BASIC_HTTP_FUNCTIONS[]
from collections import Counter
from http import HTTPStatus

import httpx
import tqdm  # type: ignore

from flags2_common import main, save_flag, DownloadStatus

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1


def get_flag(base_url: str, cc: str) -> bytes:
    url = f'{base_url}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=3.1, follow_redirects=True)
    resp.raise_for_status()  # 如果 HTTP 状态码不在 range(200, 300) 范围内，抛出 HTTPStatusError
    return resp.content


def download_one(cc: str, base_url: str, verbose: bool = False) -> DownloadStatus:
    try:
        image = get_flag(base_url, cc)
    except httpx.HTTPStatusError as exc:  # 捕获 HTTPStatusError
        res = exc.response
        if res.status_code == HTTPStatus.NOT_FOUND:
            status = DownloadStatus.NOT_FOUND  # 如果错误代码为 404，则将 status 设置为 DownloadStatus.NOT_FOUND
            msg = f'not found: {res.url}'
        else:
            raise  # 如果是其他的 Error，则抛出异常，向上冒泡
    else:
        save_flag(image, f'{cc}.gif')
        status = DownloadStatus.OK
        msg = 'OK'

    if verbose:  # 如果在命令行中设定了 -v/--verbose 选项，显示国家代码和状态消息
        print(cc, msg)

    return status


# end::FLAGS2_BASIC_HTTP_FUNCTIONS[]

# tag::FLAGS2_DOWNLOAD_MANY_SEQUENTIAL[]
def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  _unused_concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[
        DownloadStatus] = Counter()  # 这个 Counter 实例用于统计不同下载状态：DownloadStatus.OK，DownloadStatus.NOT_FOUND，DownloadStatus.ERROR
    cc_iter = sorted(cc_list)  # 按字母排序
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)  # 如果不是详细模式，就把 cc_iter 传递给 tqdm 函数，返回一个迭代器，产出 cc_iter 中的项，同时显示进度条动画。
    for cc in cc_iter:
        try:
            status = download_one(cc, base_url, verbose)  # 不断调用 download_one 函数
        except httpx.HTTPStatusError as exc:  # get_flag 抛出的异常和没有被 download_one 处理的异常，都在这里被捕捉
            error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
            error_msg = error_msg.format(resp=exc.response)
        except httpx.RequestError as exc:  # 其他网络异常在这里被捕捉，除此之外的异常会导致程序终止
            error_msg = f'{exc} {type(exc)}'.strip()
        except KeyboardInterrupt:  # 按 Ctrl + c 组合键时退出循环
            break
        else:  # 如果没有异常，则清空错误信息
            error_msg = ''

        if error_msg:
            status = DownloadStatus.ERROR  # 如果有错误，则把 status 设置为对应的状态
        counter[status] += 1  # 递增相应状态的计数器
        if verbose and error_msg:  # 如果是详细模式且有错误信息，则显示当前国家代码的错误信息
            print(f'{cc} error: {error_msg}')

    return counter  # 返回 counter，以便 main 函数能在最终报告中显示数量


# end::FLAGS2_DOWNLOAD_MANY_SEQUENTIAL[]

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
