"""Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра"""


class Archive:
    last_num = None
    last_str = None
    num_archive = []
    str_archive = []

    def __init__(self, number, text):
        self.number = number
        self.text = text
        if Archive.last_num is not None:
            Archive.num_archive.append(Archive.last_num)
        if Archive.last_str is not None:
            Archive.str_archive.append(Archive.last_str)
        Archive.last_num = number
        Archive.last_str = text


obj1 = Archive(1, 'a')
obj2 = Archive(2, 'b')
obj3 = Archive(3, 'c')
obj4 = Archive(4, 'd')

print(obj1.number, obj1.text, obj1.num_archive, obj1.str_archive)
print(obj2.number, obj2.text, obj2.num_archive, obj2.str_archive)
print(obj3.number, obj3.text, obj3.num_archive, obj3.str_archive)