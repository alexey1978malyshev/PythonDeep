'''
Взять любую задачу и настроить в ней запуск скрипта с параметрами. 
(используем Пайчарм и модуль argparse)
'''
import argparse

parser = argparse.ArgumentParser(description="Принимаем коэффициенты квадратного уравнения.")
parser.add_argument('numbers', metavar='N', type=float, nargs=3, help='Коэффициенты квадратного уравнения.')
args = parser.parse_args()


def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a == 0 or discr < 0:
        return None
    elif discr == 0:
        return -b / (2 * a)
    else:
        root_1 = (-b + discr ** 0.5) / 2 * a
        root_2 = (-b - discr ** 0.5) / 2 * a
        return root_1, root_2


print(find_roots(*args.numbers))