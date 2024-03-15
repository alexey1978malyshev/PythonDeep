"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
from typing import Callable


def counter(count: int) -> Callable:
    def launcher(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(count):
                result.append(func(*args, **kwargs) + _)
            return result

        return wrapper

    return launcher


@counter(10)
def triple_sum(a: int, b: int, c: int):
    return a + b + c


# print(triple_sum(1, 2, 3))
print(triple_sum(1, 2, 3))