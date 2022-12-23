class Pets:
    def __init__(self):
        pass

    pet_list = []

    def create_pet_list(self, *pets):
        for pet in pets:
            self.pet_list.append(pet)

    @property
    def get_pet_list(self):
        return self.pet_list


class Dog:
    mammal = 'Dog'
    nature = ''
    breed = ''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def what_dog_name(self):
        return f'Name:{self.name}  Age:{self.age}'

    @staticmethod
    def standart():
        return 'Hrr-rr-r-r, Wofff'


class Mops(Dog):
    nature = 'good'
    breed = 'mops'

    def __init__(self, name, age):
        super().__init__(name, age)

    @staticmethod
    def standart():
        return 'chawk'


class Teryer(Dog):
    nature = 'hunter'
    breed = 'teryer'

    def __init__(self, name, age):
        super().__init__(name, age)

    @staticmethod
    def standart():
        return 'i hunter woff'
