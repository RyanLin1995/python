import asyncio

import aiomysql


async def execute(host, password):
    print("开始", host)
    # 网络 IO 操作：先去连接 mysql1，遇到 IO 则自动切换任务，去连接 mysql2
    conn = await aiomysql.connect(host=host, port=3306, user='root', password=password, db='mysql')
    # 网络 IO 操作：遇到 IO 会自动切换任务
    cur = await conn.cursor()
    # 网络 IO 操作：遇到 IO 会自动切换任务
    await cur.execute('SELECT Host,User FROM user')
    # 网络IO操作：遇到IO会自动切换任务
    result = await cur.fetchall()
    print(result)
    # 网络IO操作：遇到IO会自动切换任务
    await cur.close()
    conn.close()
    print("结束", host)


task_list = [execute('127.0.0.1', 'a12345'), execute('127.0.0.1', 'a12345')]

asyncio.run(asyncio.wait(task_list))
