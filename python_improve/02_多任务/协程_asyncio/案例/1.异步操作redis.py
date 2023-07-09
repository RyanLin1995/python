import asyncio

import aioredis


async def execute(address):
    print("开始执行", address)
    # 网络Io操作：创建redis连接
    redis = await aioredis.Redis(host=address)
    # 网络io操作：在redis中设置哈希值car，内部在设三个键值对，即：redis=［car：[key1:1,key2:2,key3:3]]
    await redis.hset('car', mapping={'key1': 1, 'key2': 2, 'key3': 3})
    # 网络io操作：去redis中快取值
    result = await redis.hgetall('car')
    print(result)
    # 网络Io操作：关闭redis连接
    await redis.close()
    print("结束", address)


asyncio.run(execute('127.0.0.1'))
