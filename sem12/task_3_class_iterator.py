"""Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""

from math import factorial

class Factorial_generator():
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 1, start
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step <= 0:
            raise ValueError('Step must be a positive only')
        if self.current > self.stop:
            raise StopIteration
        res = factorial(self.current)
        self.current+=self.step
        return res

    def __str__(self):
        return f'Factorial(start={self.start}, ' \
               f'stop={self.stop}, step={self.step})'

f_gen = Factorial_generator(1,10,1)
for el in f_gen:
    print(f'{f_gen.current - f_gen.step}! = {el}')
print(f_gen)
        

