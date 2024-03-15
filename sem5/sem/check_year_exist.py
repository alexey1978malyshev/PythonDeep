'''📌 Создайте модуль и напишите в нём функцию, которая
получает на вход дату в формате DD.MM.YYYY
📌 Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
📌 Для простоты договоримся, что год может быть в диапазоне
[1, 9999].
📌 Весь период (1 января 1 года - 31 декабря 9999 года)
действует Григорианский календарь.
📌 Проверку года на високосность вынести в отдельную
защищённую функцию.'''

# __all__ = ['true_data', 'my_data']

# my_data = '01.0.2024'


# def _year_funk(year):
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print('Год високосный.')
#         return False
#     else:
#         print('Год не високосный.')
#         return True


# def true_data(data):
#     day, month, year = [int(el) for el in data.split('.')]
#     if year > 9999 or month > 12:
#         return False
#     month_30 = (4, 6, 9, 11)
#     month_31 = (1, 3, 5, 7, 8, 10, 12)
#     if month in month_30:
#         if 0 < day < 31:
#             return True
#         return False
#     elif month in month_31:
#         if 0 < day < 32:
#             return True
#         return False
#     elif month == 2:
#         if _year_funk(year):
#             if 0 < day < 29:
#                 return True
#         return False
#     else:
#         if 0 < day < 30:
#             return True
#         return False


# print(true_data(my_data))





from sys import argv

def is_leap(year: int) :
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0))

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and is_leap(year) and date > 29:
        return False
    if month == 2 and not is_leap(year) and date > 28:
        return False
    return True

if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove ))



'''Создайте пакет с всеми модулями, которые вы создали за
время занятия.
📌 Добавьте в __init__ пакета имена модулей внутри дандер
__all__.
📌 В модулях создайте дандер __all__ и укажите только те
функции, которые могут верно работать за пределами
модуля.'''