import multiprocessing


def download_data(q):
    """下载数据"""
    data = [1, 2, 3, 4]

    # 向队列写入数据
    for i in data:
        q.put(i)
    print("Data下载完成")


def processing_data(q):
    """处理数据"""
    processing_data_list = list()

    # 从队列获取数据
    while True:
        data = q.get()
        processing_data_list.append(data)
        if q.empty():
            break

    print(processing_data_list)


def main():

    # 1. 创建一个队列
    q = multiprocessing.Queue(2)

    # 2. 创建多个进程，把队列引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_data, args=(q,))
    p1.start()
    p2 = multiprocessing.Process(target=processing_data, args=(q,))
    p2.start()


if __name__ == '__main__':
    main()