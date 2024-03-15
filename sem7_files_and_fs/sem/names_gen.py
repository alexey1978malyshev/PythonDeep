'''✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.'''

import random
from pathlib import Path


def names_maker(num_of_names):
    names = []
    while num_of_names:
        name = []
        name_size = random.randint(4,7)   
        while name_size:
            sym = chr(random.randint(1072,1103))
            name.append(sym)
            name_size -= 1     
        str_name = ''.join(name)      
        names.append(str_name.title())
        num_of_names -= 1
    res = '\n'.join(names) 
    return res

with open('names.txt', 'w', encoding='utf-8') as f:
    f.write(f'{names_maker(10)}')
