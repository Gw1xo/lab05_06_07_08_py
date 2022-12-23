import random
import time


# Task 1
def area_rectangle(side_a, side_b):
    return side_a * side_b


# =========================================
# Task 2
def get_hypotenuse(leg_a, leg_b):
    return (leg_a ** 2 + leg_b ** 2) ** (1 / 2)


# =========================================
# Task 3
def get_point_list():
    lst = []
    for i in ('P', 'F', 'L'):
        print(f"\nТочка {i}:")
        for j in ('X', 'Y'):
            lst.append(float(input(f"\nВведіть координату {j} точки {i}:")))
    return lst


def get_distances(x1, y1, points):
    distances = []
    for i in (0, 2, 4):
        distances.append(((x1 - points[i]) ** 2 + (y1 - points[i + 1]) ** 2) ** (1 / 2))
    return distances


def points_inside(distances, radius):
    for i in range(3):
        match i:
            case 0:
                print("\nP:")
            case 1:
                print("\nF:")
            case 2:
                print("\nL:")

        print("В площині кола") if distances[i] <= radius else print("Не належить колу")


# =========================================
# Task 4
def quadrangle_area(sides):
    diag_xy = (sides["X"] ** 2 + sides["Y"] ** 2) ** (1 / 2)
    p = (sides["Z"] + sides["T"] + diag_xy) / 2
    area = (p * (p - sides['Z']) * (p - sides["T"]) * (p - diag_xy)) ** (1 / 2) + (sides["X"] * sides["Y"]) / 2
    return area


# =========================================
# Task 5
def get_multiples(n, numbers):
    multiples = []
    for i in range(n):
        check = True
        for item in numbers:
            if (i % item) != 0:
                check = False
        if check:
            multiples.append(i)
    multiples.remove(0)
    return multiples


# =========================================
# Task 9
def time_decorator(funct):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        funct(*args, **kwargs)
        t2 = time.perf_counter()
        print(
            f'Час виконання: {(t2 - t1):.6f}')

    return wrapper


# =========================================
# Task 6
def get_count_divisors(item):
    count = 1
    for i in range(1, item // 2 + 1):
        if item % i == 0:
            count += 1
    return count


@time_decorator
def nums_max_divisors(lst):
    max_divisors_num = lst[0]
    i = 1
    while i < len(lst):
        if get_count_divisors(max_divisors_num) < get_count_divisors(lst[i]):
            max_divisors_num = lst[i]
        i += 1

    max_divisors_nums = [i for i in lst if get_count_divisors(i) == get_count_divisors(max_divisors_num)]
    return max_divisors_nums


# =========================================
# Task 7
@time_decorator
def prime_num(n, print_mode):
    lst = [i for i in range(n) if get_count_divisors(i) <= 2]
    match print_mode:
        case 1:
            return lst
        case 2:
            return len(lst)


# =========================================
# Task 8
def generate_list(mn, mx, ln):
    return [random.randint(mn, mx) for i in range(random.randint(10, ln))]


@time_decorator
def new_list(bott, upp, lst):
    return [i for i in lst if ((max(lst) - upp) >= i) and ((min(lst) + bott) <= i)]


# =========================================
def main():
    while slct := int(input("Оберіть дію:")):
        match slct:
            case 1:
                print("\nTask 1")

                for i in range(3):
                    side_a = float(input(f"Введіть сторону А {i + 1}-го прямокутника:"))
                    side_b = float(input(f"Введіть сторону B {i + 1}-го прямокутника:"))
                    print(f"Площа {i + 1}-го прямокутника: {area_rectangle(side_a, side_b)}\n")

            case 2:
                print("\nTask 2")
                hypotenuses = []

                for i in range(2):
                    leg_a = float(input(f"\nВведіть катет А {i + 1}-го трикутника:"))
                    leg_b = float(input(f"Введіть катет B {i + 1}-го трикутника:"))

                    hypotenuses.append(get_hypotenuse(leg_a, leg_b).__round__(3))

                print(
                    f"\nГіпотенузи трикутників: {hypotenuses}"
                    f"\nНайбільша гіпотенуза: {max(hypotenuses)}"
                )

            case 3:
                print('\nTask 3')

                center_x = float(input("\nПараметри кола:\nВведіть координату Х центра:"))
                center_y = float(input("Введіть координату Y центра:"))
                radius = float(input("Введіть радіус:"))
                point_list = (get_point_list())

                points_inside(get_distances(center_x, center_y, point_list), radius)

            case 4:
                print('\nTask 4')

                sides = {'X': 0,
                         'Y': 0,
                         'Z': 0,
                         'T': 0,
                         }
                for i in ('X', 'Y', 'Z', 'T'):
                    sides[i] = float(input(f"Введіть довжину сторони {i}:"))

                print(f"Площа заданого чотирикутника: {quadrangle_area(sides)}")

            case 5:
                print('\nTask 5')

                n = int(input("Введіть N:"))
                numbers = [int(item) for item in input("Введіть числа : ").split()]

                print(f'Список кратних : {get_multiples(n, numbers)}')

            case 6:
                print('\nTask 6')

                m = int(input("Введіть M:"))
                n = int(input("Введіть N:"))

                li = range(m, n + 1)
                print(f'Числа з найбільшою кількістю дільників : {nums_max_divisors(li)}')

            case 7:
                print('\nTask 7')

                n = int(input('Введіть N'))
                print_mode = int(input('Оберіть формат: '
                                       '\n1 - список;'
                                       '\n2 - кількість;'
                                       '\nВаш вибір: '))

                print(f'Результат: {prime_num(n, print_mode)}')

            case 8:
                print(f"\nTask 8")
                lst = generate_list(random.randint(-200, 0), random.randint(0, 200), random.randint(40, 100))
                mx = max(lst)
                mn = min(lst)

                print(f'Згенерованний массив:\n{lst}')
                print(f"Максимальний елемент:{mx}\n"
                      f"Мінімальний елемент:{mn}")

                while True:
                    try:
                        upp = int(input("Введіть верхню межу:"))
                        bott = int(input("Введіть нижню межу:"))

                        if mx - upp < mn + bott or upp > mx or bott < mn:
                            raise Exception('Incorect input')
                    except ValueError:
                        print('Введіть ЦІЛЕ число!')
                    except:
                        print('Введіть коректні межі!')
                    else:
                        break

                print(f"Новий масив:\n{new_list(bott, upp, lst)}")

            case 9:
                print('\nTask 9')

                for n in (10, 100, 1000, 100000, 1000000):
                    print(f'Task 6: {n} elem')
                    nums_max_divisors(range(n))

                    print(f'Task 7: {n} elem')
                    prime_num(n, 2)

                    print(f'Task 8: {n} elem')
                    new_list(14, 14, generate_list(-200, 200, n))


if __name__ == "__main__":
    main()
