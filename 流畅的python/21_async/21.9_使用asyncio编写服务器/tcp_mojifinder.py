#!/usr/bin/env python3

# tag::TCP_MOJIFINDER_TOP[]
import asyncio
import functools
import sys
from asyncio.trsock import TransportSocket
from typing import cast

from charindex import InvertedIndex, format_results  # format_results 优化终端显示

CRLF = b'\r\n'
PROMPT = b'?> '


async def finder(index: InvertedIndex,
                 # 为了将 finder 传递给 start_server，需要用 functools.partial 包装。因为服务器预期传入的协程或函数只接受 reader 或 writer
                 reader: asyncio.StreamReader,
                 writer: asyncio.StreamWriter) -> None:
    client = writer.get_extra_info('peername')  # 获取套接字连接的远程客户端地址
    while True:  # 这个循环处理一个对话，直到从客户端收到一个控制字符
        writer.write(PROMPT)  # can't await!  # StreamWriter.write 不是协程方法，只是普通函数。
        await writer.drain()  # must await!  # StreamWriter.drain 是协程方法，刷新 writer 缓冲。
        data = await reader.readline()  # StreamWriter.readline 是协程方法，返回 bytes。
        if not data:  # 如果没有收到字节序列，则关闭客户端连接，退出循环
            break
        try:
            query = data.decode().strip()  # 使用默认的 UTF-8 编码把 bytes 转为 str
        except UnicodeDecodeError:  # 如果按了 CTRL+C 或发送了控制字节序列时，可能抛出 UnicodeDecodeError。此时把查询替换为一个空字符，简化处理
            query = '\x00'
        print(f' From {client}: {query!r}')  # 将查询输出到控制台
        if query:
            if ord(query[:1]) < 32:  # 如果收到控制字符或空字符，退出循环
                break
            results = await search(query, index, writer)  # 开始搜索
            print(f'   To {client}: {results} results.')  # 把响应输出到服务器控制台

    writer.close()  # 关闭 StreamWriter
    await writer.wait_closed()  # 等待 StreamWriter 关闭
    print(f'Close {client}.')  # 输出客户端会话终止的消息


# end::TCP_MOJIFINDER_TOP[]

# tag::TCP_MOJIFINDER_SEARCH[]
async def search(query: str,  # search 必须是协程，因为需要通过协程方法 StreamWriter.drain 写入
                 index: InvertedIndex,
                 writer: asyncio.StreamWriter) -> int:
    chars = index.search(query)  # 查询倒排索引
    lines = (line.encode() + CRLF for line
             # 这个生成器表达式产出字节字符串，使用 UTF-8 编码 Uicode码点、字符本身、字符名称和CRLF序列，例如 b'U+0039\t9\tDIGIT NINE\rn'
             in format_results(chars))
    writer.writelines(lines)
    await writer.drain()
    status_line = f'{"─" * 66} {len(chars)} found'  # 构建状态行，然后发送
    writer.write(status_line.encode() + CRLF)
    await writer.drain()
    return len(chars)


# end::TCP_MOJIFINDER_SEARCH[]

# tag::TCP_MOJIFINDER_MAIN[]
async def supervisor(index: InvertedIndex, host: str, port: int) -> None:
    server = await asyncio.start_server(  # start_server 可以快速创建一个 TCP 套接字服务器
        functools.partial(finder, index),  # start_server 的第一个参数 client_connected_cb 是一个回调，在客户端发起新连接时运行。
        # 这个回调可以是普通函数，也可以是协程，不过必须接受两个参数，一个是 asyncio.streamReader 对象，另一个是 asyncio.Streamwriter 对象。
        # 而 finder 协程还需要获取 index，因此使用 functools.partial 绑定该参数，得到一个接受asyncio.StreamReader 和 asyncio.StreamWriter 对象的回调。
        # 为适应回调 API 而改造用户函数是 functools.partial 最常见的用途之一。
        host, port)  # start_server 的第二个和第三个参数是 host和 port。

    socket_list = cast(tuple[TransportSocket, ...],
                       server.sockets)  # 这里有必要调用 cast，因为 typeshed 为 Server 类的 sockets 特性提供的类型提示还是过时的。详见 typeshed 项目的 5535 号工单。
    addr = socket_list[0].getsockname()
    print(f'Serving on {addr}. Hit CTRL-C to stop.')  # 显示服务器第一个套接字的地址和端口
    await server.serve_forever()  # 虽然 start_server 是以并发任务启动服务器的，但这里还是要使用 await 处理 server.forever 方法，
    # 目的是让 supervisor 协程在这里中止。倘若没有这一行，supervisor 将立即返回，终止 asyncio.run(supervisor(...)) 启动的循环，导致程序退出。
    # Server.serve_forever 的文档指出，“服务器已经开始接收连接后，可以调用这个方法”。


def main(host: str = '127.0.0.1', port_arg: str = '2323'):
    port = int(port_arg)
    print('Building index.')
    index = InvertedIndex()  # 构建倒排索引。
    try:
        asyncio.run(supervisor(index, host, port))  # 启动事件循环，运行 supervisor
    except KeyboardInterrupt:  # 捕获 KeyboardInterrupt，防止在终端按 Ctrl-C 停止服务器时输出太多调用跟踪，扰乱视线
        print('\nServer shut down.')


if __name__ == '__main__':
    main(*sys.argv[1:])
# end::TCP_MOJIFINDER_MAIN[]
