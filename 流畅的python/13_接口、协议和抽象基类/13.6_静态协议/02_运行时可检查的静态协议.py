from typing import SupportsComplex
import numpy as np

c64 = np.complex64(3 + 4j)  # 使用 complex64 定义一个复数类型
print(isinstance(c64, complex))  # numpy 的 complex64 不是内置类型 complex 的子类
print(isinstance(c64, SupportsComplex))  # 但是 numpy 的 complex64 实现了 __complex__ 方法，因此符合 SupportsComplex 协议
c = complex(c64)  # 因此可以使用 numpy 中的复数类型创建内置的 complex 对象
print(c)
print(isinstance(c, SupportsComplex))  # 但是内置 complex 对象没有实现 __complex__ 方法。
print(complex(c))  # 但 c 是一个 complex 值，可以得到正确结果
print(isinstance(c, (complex, SupportsComplex)))  # 可以测试对象是否为其中一个类型
