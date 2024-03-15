'''✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.'''

from pathlib import Path
import random


def fill_file_random_num(num: int, path: Path):
    count = 0
    with open(path, 'w', encoding='utf-8') as f:
        while count< num:
            f.write(f'{random.randint(-1000,1000)} | {random.uniform(-1000,1000)}\n')
            count +=1


fill_file_random_num(10,'new_f.txt')