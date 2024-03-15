'''📌Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
📌Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
📌Имена пишите с большой буквы.
📌Каждую пару сохраняйте с новой строки.'''

import json

def txt_to_json(f_txt, f_json):
    with(open(f_txt, 'r', encoding='utf-8') as f_read,
        open(f_json, 'w', encoding='utf-8')as f_write
        ):
        data = {}
        for line in f_read:
            data[line.split()[0].capitalize()] = line.split()[1]
        json.dump(data, f_write, indent=2)
    

txt_to_json('names_val.txt', 'names_val.json')