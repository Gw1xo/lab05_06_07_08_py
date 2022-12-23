import os
import pathlib
from pathlib import Path


# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()


workdir_path = Path.joinpath(dir_path, 'task4_result')
garbage_file = Path(workdir_path, 'garbage_file.txt')

if os.path.isdir(workdir_path):
    os.remove(garbage_file)
    os.rmdir(workdir_path)

if not os.path.isdir(workdir_path):
    os.mkdir(workdir_path)

# Об'єднуємо шлях до робочої директорії з файлом
learning_python_path = Path.joinpath(dir_path, 'learning_python.txt')

lines = []

with open(garbage_file, 'w'):
    print()

with Path.open(learning_python_path, 'r', encoding='UTF-8') as learn_file:
    for line in learn_file:
        lines.append(line.replace('Python', 'C#'))

with open(learning_python_path, 'w') as file:
    for line in lines:
        print(line + '\n')
        if answer := input("It`s true?") == 'Yes':
            file.write(line)
        else:
            with open(garbage_file, 'a') as wr_file:
                wr_file.write(line)

