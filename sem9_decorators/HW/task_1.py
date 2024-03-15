import csv
import json
from pathlib import Path
from random import randint

FILE_NAME = 'new_f.csv'

def save_to_json(func):
    def wrapper(*args):
        with open(Path(FILE_NAME), 'r', newline='', encoding='utf-8') as source:
            csv_reader = csv.reader(source, quoting=csv.QUOTE_NONE)
            data = [[int(a), int(b), int(c)] for a, b, c in csv.reader(source)]
            res = []
            for a, b, c in data:
                entry = {'parameters': [a, b, c], 'result': func(a, b, c)}
                res.append(entry)
        with open(Path('results.json'), 'w', encoding='utf-8') as file:
            json.dump(res, file)

    return wrapper


def generate_csv_file(file_name, rows):
    if 100 > rows > 1000:
        return
    res = []
    for _ in range(rows):
        res.append([randint(-100, 100), randint(-100, 100), randint(-100, 100)])
    with open(Path(file_name), 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(res)


@save_to_json
def find_roots(a, b, c):
    discr = b ** 2 - 4 * a * c
    if a == 0 or discr < 0:
        return None
    elif discr == 0:
        return -b / (2 * a)
    else:
        root_1 = (-b + discr ** 0.5) / 2 * a
        root_2 = (-b - discr ** 0.5) / 2 * a
        return root_1, root_2


#generate_csv_file(FILE_NAME, 3)
find_roots()