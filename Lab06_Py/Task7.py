import csv
import re
import pathlib
from pathlib import Path
from datetime import datetime
import time

# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()

# Створюємо шлях до файлу
src_path = Path(dir_path, 'task7_dir', 'marks.lab6.csv')

# Відкриваємо файл і зчитуємо дані
data = []
with open(src_path, 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# визначаємо кількість студентів
count_stud = len(data)
# print(count_stud)

# Змінимо сепаратор для дробових значень
for row in data:
    i = 4
    while i < len(row):
        row[i] = row[i].replace(',', '.')
        i += 1

# Створимо словник студентів з оцінками
result = {}
for row in data:
    result[row[0]] = float(row[4])

# переведемо час виконання в секунди
