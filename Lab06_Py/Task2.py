import os
import pathlib
from pathlib import Path


# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()

# Об'єднуємо шлях до робочої директорії з результуючим файлом
res_file_path = Path.joinpath(dir_path, 'result_file.txt')

# Якщо файл існує видаляємо його
if os.path.exists(res_file_path):
    os.remove(res_file_path)

with Path.open(res_file_path, 'w') as file:
    while num := int(input('Введіть число для завершення програми введіть 0\n')):
        file.write(f'Число {num} - парне\n') if num % 2 == 0 else file.write(f'Число {num} - непарне\n')