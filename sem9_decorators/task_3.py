"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""

import json
from typing import Callable
from pathlib import Path
from inspect import signature

_PATH = Path.cwd() 


def save_to_json(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        entry = {k: v for k, v in
                 [(i, j) for i, j in zip(signature(func).parameters.keys(), args + tuple(kwargs.values()))]}
        entry['result'] = result
        filepath = Path(_PATH, func.__name__ + '.json')

        if not filepath.is_file():
            with open(filepath, 'w', encoding='utf-8') as file:
                data = [entry]
                json.dump(data, file, indent=2)
        else:
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                data.append(entry)
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2)
        return result

    return wrapper


@save_to_json
def triple_sum(a: int, b: int, *, c: int):
    return a + b + c


triple_sum(-1100, 200, c=900)