from BankClass import Bank
from CoinClass import Coin
from CarClass import Car
import DogClass
from BufferClass import Buffer
from NameErrorClass import NameError
import romanconvecter
from ShopClass import Shop, Discount
from UserClass import User
from PrivilegesClass import Admin


def task1():
    bank = Bank(2300)
    print(bank.check_balance())
    print(bank.withdrawal(2500))
    print(bank.check_balance())
    print(bank.add_to_balance(200))
    print(bank.check_balance())
    print(bank.withdrawal(500))
    print(bank.check_balance())


def task2():
    coin = Coin()
    for i in range(50):
        print(coin.toss())


def task3():
    car = Car('Toyota', 'Camry')
    for acs in range(5):
        print(car.accelerate)
    for brc in range(5):
        print(car.brake)


def task4():
    pets = DogClass.Pets()
    pets.create_pet_list(DogClass.Mops('Kivi', '2'), DogClass.Teryer('Spaike', '3'), DogClass.Dog('Gerda', '1'))
    pet: DogClass.Dog
    for pet in pets.get_pet_list:
        print('____________________________')
        print(f"{pet.nature}------{pet.breed}")
        print(pet.what_dog_name())
        print(pet.standart())


def task5():
    buffer = Buffer()
    print("Add 3 elem")
    print(buffer.add(2, 3, 4))
    print(buffer.get_current_part())
    print('Add 4 elem')
    print(buffer.add(3, 4, 5, 6))
    print(buffer.get_current_part())


def task6():
    name = input('Enter name:')
    if len(name) < 10:
        raise NameError("Дуже коротке ім'я")


def task7():
    to_roman = romanconvecter.IntToRoman()
    to_dec = romanconvecter.RomanToInt()
    roman_num = to_roman.dec_to_roman(int(input('Введiть число: ')))
    print(roman_num)
    dec_num = to_dec.roman_to_dec(input('Введіть римське число: '))
    print(dec_num)


def task8():
    # a
    store = Shop('LoliShop', 'CostPlay')
    print(store.shop_name)
    print(store.shop_type)
    print(store.describe_shop())
    print(store.open_shop())
    # b
    store1 = Shop('Delfini', 'market')
    store2 = Shop('PiisiPig', 'zoomarket')
    store3 = Shop('AngelCookie', 'candymarket')
    print(store1.describe_shop())
    print(store2.describe_shop())
    print(store3.describe_shop())
    # c
    print(store.number_of_units)
    store.number_of_units = 3
    print(store.number_of_units)
    # d
    store.set_number_units(4)
    print(store.number_of_units)
    store.increment_number_of_units(2)
    print(store.number_of_units)
    # e
    store_discount = Discount('Велвет', 'supermarket', 'Банан', 'Молоко', 'Сир')
    print(store_discount.get_discount_products())
    # f
    all_store = Shop('All store', 'store')
    all_store.open_shop()


def task9():
    # a
    user1 = User('Jonn', 'Billygan', 'email@email.com', 'misterkreativ', False)
    user2 = User('Jesica', 'Billygan', 'email1@email.com', 'misiskreativ', True)
    print(f'{user1.describe_user}\n{user2.describe_user}')
    print(f'{user1.greeting_user}\n{user2.greeting_user}')
    # b
    for i in range(4):
        user1.increment_logit_attempts()
    print(user1.login_attempts)
    user1.reset_login_attempts()
    print(user1.login_attempts)
    # c
    admin = Admin('Cool', 'boy', 'di@email.com', 'cool_boy', False)
    for privilege in admin.show_privileges:
        print(privilege)
    # d
    priv = admin
    for privilege in admin.show_privileges:
        print(privilege)


if __name__ == "__main__":
    task9()
