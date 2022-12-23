import pathlib
from pathlib import Path

learn_python_list = []

# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()

# Об'єднуємо шлях до робочої директорії з файлом
learning_python_path = Path.joinpath(dir_path, 'learning_python.txt')

# Відкриваємо файл для читання та записуємо рядки в список
with Path.open(learning_python_path, 'r', encoding='UTF-8') as file:
    for line in file:
        print(line)
        learn_python_list.append(line)

learn_python_list.sort(key=lambda x: len(x), reverse=True)
print(learn_python_list)
