"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def guess_num(tries: int = 5, num: int = 50):
    def prompt():
        nonlocal tries, num
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

    return prompt


game = guess_num(5, 75)
game()

# from random import randint as ri
#
# MIN_LIMIT = 1
# MAX_LIMIT = 100
# MIN_COUNT = 1
# MAX_COUNT = 10
#
#
# def guess_rules(func):
#     def inner(number, count):
#         user_number = number if MIN_LIMIT <= number <= MAX_LIMIT else ri(MIN_LIMIT, MAX_LIMIT)
#         user_count = count if MIN_COUNT <= count <= MAX_COUNT else ri(MIN_COUNT, MAX_COUNT)
#         func(user_number, user_count)
#
#     return inner
#
#
# @guess_rules
# def guess_game(user_number, user_count):
#     while user_count:
#         guess_num = int(input(f'Угадайте число от {MIN_LIMIT} до {MAX_LIMIT}: '))
#         if guess_num == user_number:
#             print(f'Ура, ты победил! Это число {user_number}')
#             return
#         elif guess_num < user_number:
#             print('Загаданное число больше!')
#         else:
#             print('Загаданное число меньше!')
#         user_count -= 1
#     print(f'Увы! Ты проиграл! Это было число {user_number}!')
#
#
# if __name__ == '__main__':
#     game = guess_rules(169, 7)
#     game()