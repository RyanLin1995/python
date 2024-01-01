#!/usr/bin/env python3

"""Download flags of countries (with error handling).

ThreadPool version

Sample run::

    $ python3 flags2_threadpool.py -s ERROR -e
    ERROR site: http://localhost:8003/flags
    Searching for 676 flags: from AA to ZZ
    30 concurrent connections will be used.
    --------------------
    150 flags downloaded.
    361 not found.
    165 errors.
    Elapsed time: 7.46s

"""

# tag::FLAGS2_THREADPOOL[]
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import httpx
import tqdm  # type: ignore

from flags2_common import main, DownloadStatus
from flags2_sequential import download_one  # 重复利用 download_one 函数

DEFAULT_CONCUR_REQ = 30  # 如果没有在命令行中指定 -m/--max_req 选项，则使用这个值作为并发请求数的最大值也就是线程池的大小;真实的数量可能会比这少
MAX_CONCUR_REQ = 1000  # 不管要下载多少国旗，也不管 -m/--max_req 命令行选项的值是多少，MAX_CONCUR_REQ会限制最大的并发请求数。这是一项安全措施，免得启动太多线程，消耗过多内存


def download_many(cc_list: list[str],
                  base_url: str,
                  verbose: bool,
                  concur_req: int) -> Counter[DownloadStatus]:
    counter: Counter[DownloadStatus] = Counter()
    with ThreadPoolExecutor(
            max_workers=concur_req) as executor:  # 把 max_workers 设为 concur_req，创建 executor。main 函数会把下面这 3 个值中最小那个赋给 concur_req: MAX_CONCUR_REQ、cc_ist 的长度、-m/--max_req 命令行选项的值。这样能避免创建过多的线程
        to_do_map = {}  # 这个字典把各个 Future 实例(表示一次下载)映射到相应的国家代码上，在处理错误时使用
        for cc in sorted(
                cc_list):  # 按字母表顺序迭代国家代码列表。结果的顺序主要由 HTTP 响应的时间长短决定，不过，如果线程池的大小(由concur_req 设定) 比 Len(cc_list)小得多，那么可能会按字母表顺序批量下载
            future = executor.submit(download_one, cc,
                                     base_url,
                                     verbose)  # 每次调用 executor.submit 方法排定一个可调用对象的执行时间，返回一个 Future 实例。第一个参数是可调用对象，余下的参数是传给可调用对象的参数
            to_do_map[future] = cc  # 把返回的 future 和国家代码存储在字典中
        done_iter = as_completed(to_do_map)  # futures.as_completed 函数返回一个迭代器，在每个任务运行结束后产出 future 对象
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(
                cc_list))  # 如果不是详细模式，则把 as_completed 函数返回的结果传给 tqdm 函数，显示进度条；因为 done_iter 没有长度，所以我们必须通过 total= 参数告诉 tqdm 函数预期的项数这样 tqdm 才能预计剩余的工作量
        for future in done_iter:  # 迭代运行结束后的 future对象
            try:
                status = future.result()  # 在future对象上调用 result 方法，要么返回可调用对象的返回值，要么抛出可调用对象在执行过程中捕获的异常。这个方法可能会阻塞，等待确定结果，但是，在这个示例中不阻塞，因为as_completed 函数只返回已经运行结束的 future 对象。
            except httpx.HTTPStatusError as exc:  # 异常捕获
                error_msg = 'HTTP error {resp.status_code} - {resp.reason_phrase}'
                error_msg = error_msg.format(resp=exc.response)
            except httpx.RequestError as exc:
                error_msg = f'{exc} {type(exc)}'.strip()
            except KeyboardInterrupt:
                break
            else:
                error_msg = ''

            if error_msg:
                status = DownloadStatus.ERROR
            counter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[
                    future]  # 为了给错误消息提供上下文，以当前的 future 为键，从 to_do_map 中获取国家代码。在依序下载版中无须这么做，因为那一版迭代的是国家代码，知道当前国家代码是什么，而这里迭代的是 future 对象。
                print(f'{cc} error: {error_msg}')

    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
# end::FLAGS2_THREADPOOL[]
