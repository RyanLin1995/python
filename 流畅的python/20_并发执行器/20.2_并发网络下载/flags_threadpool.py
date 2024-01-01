from concurrent import futures

from flags import save_flag, get_flag, main


def download_one(cc: str):  # 这里的函数是 flags 中的 download_many for 循环体。编写并发代码时经常需要这样重构：把依序执行的 for 循环改成函数，并发调用
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor() as executor:  # 实例化 ThreadPoolExecutor，作为上下文管理器，有 max_workers 参数，用于设置最多执行多少个工作线程。executor.__exit__ 方法将调用 executor.shutdown(wait=True)，在所有线程都执行完毕前阻塞线程
        res = executor.map(download_one, cc_list)

    return len(list(res))


if __name__ == '__main__':
    main(download_many)
