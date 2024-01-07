import asyncio


async def raise_error():
    raise EOFError


async def main():
    coros = raise_error()
    for coro in asyncio.as_completed(coros):
        print(coro)
