"""Задание №2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""

import json
from pathlib import Path
from math import factorial


class Facto:
    def __init__(self, k, path):
        self.storage = {}
        self.path = path
        self.k = k

    def __str__(self):
        return ', '.join(f'{k}:{v}' for k, v in sorted(self.storage.items()))

    def __call__(self, value):
        for _ in range(self.k):
            self.storage[value] = factorial(value)
            value -= 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(sorted(self.storage), file)


if __name__ == '__main__':
    a = Facto(4, Path(Path.cwd() / 'test.json'))
    a(10)
    print(a)
    print(a)

    with a:
        print('lele')