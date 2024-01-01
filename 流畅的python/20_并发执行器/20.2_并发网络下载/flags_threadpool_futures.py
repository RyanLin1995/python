from concurrent import futures

from flags import save_flag, get_flag, main


def download_one(cc: str):  # 这里的函数是 flags 中的 download_many for 循环体。编写并发代码时经常需要这样重构：把依序执行的 for 循环改成函数，并发调用
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one,
                                     cc)  # executor.submit 方法排定可调用对象的执行时间（即添加futures任务队列），返回一个future对象，表示待执行的操作。
            to_do.append(future)  # 存储各个 future 对象，后面传给 as_completed 函数
            print(f'Scheduled for {cc}: {future}')

        for count, future in enumerate(futures.as_completed(
                to_do)):  # as_completed 函数在 future 对象运行结束后产出 future 对象。as_completed() 方法是一个生成器，在任务没有完成的时候，会阻塞，在有某个任务完成的时候，会 yield 这个任务，就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，先完成的任务会先通知主线程。
            res: str = future.result()  # 获取 future 对象结果。因为 future 由 as_completed 函数产生，所以这里不会阻塞
            print(f'{future} result: {res!r}')
    return count


if __name__ == '__main__':
    main(download_many)
