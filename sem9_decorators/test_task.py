from typing import Callable

class Deco:
    def __init__(self, num: int):
        self.num = num
    def __call__(self, func: Callable):
        def wrapper():
            return func()
        return wrapper


@Deco(5)
def my_func():
    return "Hello world"

print(my_func())