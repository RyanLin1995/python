import asyncio

import aioredis
import uvicorn
from aioredis import Redis
from fastapi import FastAPI

app = FastAPI()
# 创建一个redis连接池
REDIS_POOL = aioredis.ConnectionPool.from_url('redis://127.0.0.1', max_connections=10)


@app.get("/")
def index():
    """普通操作接口"""
    return {"message": "Hello world"}


@app.get("/red")
async def red():
    """异步操作接口"""
    print("请求来了")
    await asyncio.sleep(3)
    # 连接池获取一个连接
    redis = Redis(connection_pool=REDIS_POOL)
    # 设置值
    await redis.hset('car', mapping={'key1': 1, 'key2': 2, 'key3': 3})
    # 读取值
    result = await redis.hgetall('car')
    print(result)
    await redis.close()
    # 连接归还连接池
    return result


if __name__ == '__main__':
    uvicorn.run(f'{__name__}:app', host="127.0.0.1", port=5000, log_level="info")
