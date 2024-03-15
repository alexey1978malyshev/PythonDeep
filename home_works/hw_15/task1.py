'''
Задание №6
Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
В процессе сбора сохраните данные в текстовый файл используя
логирование
'''

from collections import namedtuple
from pathlib import Path

from logger import log

PATH = Path('C:\\', 'Study', 'Python_2', 'homeworks', 'hw_15', 'task_1')
LOG_PATH = Path.cwd() / 'log.txt'


def get_dir_info(path: Path, logfile: Path):
    PathObject = namedtuple('PathObject', ('name', 'extension', 'is_dir', 'parent'))
    parent = path.parts[-1]
    for item in path.iterdir():
        if item.is_file():
            name = item.name[:item.name.rfind('.')]
            extension = item.name[item.name.rfind('.') + 1:]
            entry = PathObject(name, extension, item.is_dir(), parent)
            log(str(entry), logfile)
        else:
            entry = PathObject(item.name, None, item.is_dir(), parent)
            log(str(entry), logfile)


if __name__ == '__main__':
    get_dir_info(PATH, LOG_PATH)