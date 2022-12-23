import pathlib
from pathlib import Path
from datetime import datetime
import time
import re


def time_decorator(funct):
    def wrapper(text1, text2):
        t1 = time.perf_counter()
        res = funct(text1, text2)
        t2 = time.perf_counter()
        return res + f'Час пошуку: {(t2 - t1):.6f}'
    return wrapper


@time_decorator
def find_statistic(search, text):
    return f'{search} : {len(re.findall(search, text))}'


def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()
# Створюємо шлях до файлу
publication_path = Path(dir_path, 'publication_python')
char_stat_path = Path(dir_path, 'char_statistic.txt')

with open(char_stat_path, 'w') as mk_file:
    mk_file.write('Дата створення:' + get_datetime() + '\n')

super_string = ''

with Path.open(publication_path) as file:
    for line in file:
        super_string += line

word = input('Введіть слово чи букву для пошуку:')

with open(char_stat_path, 'a') as statistic:
    statistic.write('Change:' + get_datetime() + '\n' + find_statistic(word, super_string) + '\n')


