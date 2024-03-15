'''Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.'''


list_names = []
list_nums = []


with( 
    open('names.txt', 'r', encoding='utf-8') as f1,
    open('new_f.txt', 'r', encoding='utf-8') as f2

):
    for el in f1:
        list_names.append(el.strip('\n'))
    
    for el in f2:
        new_el = el.split('|')
        list_nums.append(round(int(new_el[0]) * float(new_el[-1]), 2))

#print(list_names)
res = dict(zip(list_names,list_nums))
print(res)
res = {(k.lower() if v < 0 else k.upper()):(abs(v) if v < 0 else int(v)) for k,v in res.items()}
print(res)

with open('sem8/names_val.txt', 'w',encoding='utf-8') as f:
    for k,v in res.items():
     f.writelines(f'{k} {v}\n')

