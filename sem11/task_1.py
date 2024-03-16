'''Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''
import os
import time


class MyStr(str):
    """Modified 'str' class with creation time and author(login)."""

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        #instance.creation_time = time.time()
        instance.login = os.getlogin()
        return instance
    
    def __init__(self, text):
        self.text = text
        self.time = time.time()



text = MyStr('Kkwrgire[ainb')
# print(text)
# print(text.login)
# print(text.name)
# print(text.time)
a = MyStr('jjj')
print(a.login, a.text)
