"""
Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""
import logging
import datetime

PATH = 'history.log'


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.basicConfig(level=logging.NOTSET, filename=PATH, filemode='a')
        logger = logging.getLogger(__name__)
        logger.info(f'{datetime.datetime.now()} | args: {args} | result: {result}')
        return result

    return wrapper


@log
def function(a, b):
    return a + b


function(5, 3)