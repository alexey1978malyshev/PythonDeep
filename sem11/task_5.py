"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""
from math import sqrt


class Rectangle:
    def __init__(self, *args):
        self._length = args[0]
        self._width = self._length if len(args) == 1 else args[1]

    @property
    def area(self):
        return self._length * self._width

    @property
    def perimeter(self):
        return 2 * (self._length + self._width)

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    def __add__(self, other):
        return Rectangle(sqrt(self.perimeter + other.perimeter))

    def __sub__(self, other):
        return Rectangle(sqrt(abs(self.perimeter - other.perimeter)))

    def __str__(self):
        return f'length= {self.length:.3f}, width= {self.width:.3f}'


a = Rectangle(2, 5)
b = Rectangle(7, 3)
c = a - b
print(c)