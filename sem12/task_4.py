"""Задание №6
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера"""


class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError('Неверный формат данных')
        if value <= 0:
            raise ValueError('Стороны должны быть положительными')


class Rectangle:
    # __slots__ = '_length', '_width'
    length = Range() # - это дескрипторы
    width = Range()

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'


a = Rectangle(5, 4)
print(a.__dict__)