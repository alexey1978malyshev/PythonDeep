"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
import json
from functools import wraps
from typing import Callable
from random import randint
from pathlib import Path
from inspect import signature

_PATH = Path.cwd() / 'tasks_3_4'


def check_ranges(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args):
        if 1 <= args[0] <= 10 and 1 <= args[1] <= 100:
            return func(args[0], args[1])
        print('Generating random arguments.')
        return func(randint(1, 10), randint(1, 100))

    return wrapper


def save_to_json(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args):
        result = func(*args)
        entry = {k: v for k, v in
                 [(i, j) for i, j in zip(signature(func).parameters.keys(), args)]}
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


def counter(count: int) -> Callable:
    def launcher(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(count):
                result.append(func(*args, **kwargs) + _)
            return result

        return wrapper

    return launcher


@save_to_json
@check_ranges
@counter(3)
def prompt(tries: int, num: int):
    while tries > 0:
        print(f'Осталось {tries} попыток.')
        attempt = int(input('Введите число:\n'))
        if attempt == num:
            print('Вы угадали.')
            return True
        else:
            print('Вы не угадали.')
            tries -= 1
            if tries == 0:
                print('Попытки закончились.')
                return False


prompt(5, 50)
# from random import randint
# import functools
# import json
#
# my_list = []
#
#
# def control_param_decorator(func):
#     @functools.wraps(func)
#     def wrapper(count):
#         global hidden_num
#         hidden_num = int(input('Задайте число от 1 до 100: '))
#         if not 0 < hidden_num < 101:
#             hidden_num = randint(1, 100)
#         global attempts_num
#         attempts_num = int(input('Установите число попыток от 1 до 10: '))
#         if not 0 < attempts_num < 11:
#             attempts_num = randint(1, 10)
#         result = func(count, hidden_num, attempts_num)
#         print(result)
#         return result
#
#     return wrapper
#
#
# def save_param_decorator(func):
#     @functools.wraps(func)
#     def wrapper(count):
#         result = func(count)
#         result_dict = {f'{hidden_num, attempts_num}': result}
#         my_list.append(result_dict)
#         with open(f'{func.__name__}.json', 'w', encoding='utf-8') as f:
#             json.dump(my_list, f, ensure_ascii=False)
#         return result
#
#     return wrapper
#
#
# def count_func(func):
#     @functools.wraps(func)
#     def wrapper(count):
#         for _ in range(count):
#             func(count)
#
#     return wrapper
#
#
# # @count_func
# # @save_param_decorator
# # @control_param_decorator
# def guess_num(count, hidden_num=0, attempts_num=0):
#     for _ in range(attempts_num):
#         user_num = int(input('Введите своё число: '))
#         if user_num == hidden_num:
#             return 'Вы угадали!'
#     return 'Попытки закончились, вы не угадали!'
#
#
#
# count_func(save_param_decorator(control_param_decorator(guess_num)))(3)