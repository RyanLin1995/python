@REM 定义和使用一个异步生成器表达式
cd 'E:\learning\python\流畅的python\21_async\21.10_异步迭代和异步可迭代对象'
python -m asyncio
names = 'python.org rust-lang.org golang.org no-lang.invalid'.split()
from domainlib import multi_probe
gen_found = (name async for name, found in multi_probe(names) if found)
gen_found
async for name in gen_found:
...     print(name)
...

@REM 异步推导式
import asyncio
names = 'python.org rust-lang.org golang.org no-lang.invalid'.split()
from domainlib import probe, multi_probe
names = sorted(names)
@REM 在列表推导式中使用 await，作用类似于 asyncio.gather。但 asyncio.gather 接受一个可选参数 return_exceptions，用于进一步处理异常
coros = [probe(name) for name in names]
await asyncio.gather(*coros)
[Result(domain='golang.org', found=True), Result(domain='no-lang.invalid', found=False), Result(domain='python.org', found=True), Result(domain='rust-lang.org', found=True)]
[await probe(name) for name in names]
[Result(domain='golang.org', found=True), Result(domain='no-lang.invalid', found=False), Result(domain='python.org', found=True), Result(domain='rust-lang.org', found=True)]
@REM 在字典和集合中也可以使用 async for 和 await
{name:found async for name, found in multi_probe(names)}
{'golang.org': True, 'rust-lang.org': True, 'python.org': True, 'no-lang.invalid': False}
@REM 在 for 或 async for 子句前面，以及 if 子句后面，可以使用 await 关键字。由于 _getattr_运算符.(点号) 的优先级较高，因此要在 await 表达式两侧再加一层括号
{name for name in names if (await probe(name)).found}
{'python.org', 'golang.org', 'rust-lang.org'}

