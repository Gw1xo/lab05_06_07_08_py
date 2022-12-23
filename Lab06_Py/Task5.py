import pathlib
from pathlib import Path
from datetime import datetime


def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string


# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()
# Створюємо шлях до файлу
guest_path = Path(dir_path, 'guest_book.txt')

with open(guest_path, 'w') as guest_file:
    guest_file.write('Створено: ' + get_datetime() + '\n')

while (line := input('0 - Завершити роботу\n Введіть дію або ім\'я для запису:')) != '0':
    with open(guest_path, 'a') as guest_file:
        guest_file.write(f"----Hello,{line}----" + get_datetime() + '\n')
        print(f"----Hello,{line}----")

