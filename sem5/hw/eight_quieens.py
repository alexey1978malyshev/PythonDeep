'''Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens),
 которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину, а если бьют - ложь. '''


queens = [(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)]

def is_attacking(q1,q2):
    flag = True   
      
    # for i in q1:
    #     for j in q2:
    #         if i == j:
    #             flag = False

    if q1[0] == q2[0] or q1[1] == q2[1]:
        flag = False
    
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        flag = False       

    return flag

#print(is_attacking((1, 1), (8, 2)))

def check_queens(queens):
    flag = True
    for i in range(len(queens)-1):
        for j in range(i + 1, len(queens)):
            if not is_attacking(queens[i], queens[j]):
                flag = False
                return flag        
    return flag



#print(check_queens(queens))

'''Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
 Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка
 ферзей на шахматной доске, в которой ни один ферзь не бьет другого. Другими словами, 
 ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали 
 или диагонали.

Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо. '''

import random

def generate_boards():
    board_list = []
    while len(board_list) < 4:
        try_lst = []
        set_abc = set()
        set_ord = set()
        while len(try_lst) < 8:
            new_coord = (random.randint(1,8), random.randint(1,8))
            
            if len(try_lst) <= 1:
                try_lst.append(new_coord)
                set_abc.add(new_coord[0])
                set_ord.add(new_coord[1])
                
            if  new_coord[0] not in set_abc and new_coord[1] not in set_ord:
                try_lst.append(new_coord) 
                set_abc.add(new_coord[0])
                set_ord.add(new_coord[1])                
                                                                             
            else:                   
               continue
        if check_queens(try_lst) == True:
            board_list.append(try_lst)        

    return board_list

print(generate_boards())


'''"эталонное" решение'''
import random
from itertools import combinations

def generate_board():
    # Генерируем случайную доску
    board = []

    for i in range(1, 8+1):
        queen = (i, random.randint(1, 8))
        board.append(queen)
    return board

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True

def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 0
    board_list = []
    while count < 4:
        board = generate_board()
        if check_queens(board):
            count += 1
            board_list.append(board)
    return board_list

