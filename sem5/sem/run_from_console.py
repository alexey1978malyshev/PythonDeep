'''📌 Улучшаем задачу 2.
📌 Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
📌 Строка должна принимать от 1 до 3 аргументов: параметры
вызова функции.
📌 Для преобразования строковых аргументов командной
строки в числовые параметры используйте генераторное
выражение.'''

from guess_number import guess_number
from sys import argv

print(argv)
data = (int(a) for a in argv[1:])
print(data)

print(guess_number(*data))