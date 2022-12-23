import pathlib
from pathlib import Path

nums = []

# Отримуємо рядок до робочої директорії:
dir_path = pathlib.Path.cwd()

# Об'єднуємо шлях до робочої директорії з файлом з числами
nums_path = Path.joinpath(dir_path, 'numbers.txt')

# Об'єднуємо шлях до робочої директорії з результуючим файлом
sum_path = Path.joinpath(dir_path, 'sum_numbers.txt')

with Path.open(nums_path, 'r') as file_nums:
    for line in file_nums:
        nums.append(int(line))

sum_num = sum(nums)

with Path.open(sum_path, 'w') as file_sum:
    file_sum.write(f'{sum_num}')
    print(sum_num)
