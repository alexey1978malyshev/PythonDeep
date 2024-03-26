# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


from logger import log


def func(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        log('error', f'func({a}, {b}) | {e}')
        return f'{a} / {b} | {e}'


print(func(10, 0))