import datetime
import json


def format_date(date):
    # функція для переведення рядка в дату
    return [int(i) for i in date.split('-')]


class Person:
    """
    Клас реалізує запис в книзі контактів
    """

    def __init__(self, surname: str, first_name: str, birth_date: str, nickname: str = ''):
        """
        type surname: str
        type first_name: str
        type birth_date: datetime.date()
        type nickname: str
        """
        day, mon, year = format_date(birth_date)
        self.surname = surname
        self.first_name = first_name
        self.birth_date = datetime.date(year, mon, day)
        self.nickname = nickname

    def get_age(self):
        """
        Повертає кількість повних років користувача
        """
        now_date = datetime.date.today()
        tmp = now_date - self.birth_date
        day_year = 365  # Кількість днів в році
        return tmp.days // day_year

    def get_fullname(self):
        """
        Повертає повне ім'я контакту
        """
        return f'{self.surname} {self.first_name}'


def modifier(filename, persons: []):
    extend_user_data = {'person': []}
    pers: Person
    for pers in persons:
        extend_user_data['person'].append(
            {
                'Surname': pers.surname,
                "Firstname": pers.first_name,
                'Fullname': pers.get_fullname(),
                "Birthdate": str(pers.birth_date),
                "Nickname": pers.nickname,
                "Age": pers.get_age(),
            }
        )
    with open(filename, 'w') as extend_data:
        json.dump(extend_user_data, extend_data)


def create_datafile():
    user_data = {'person': []}
    user_data['person'].append(
        {
            'Surname': 'Jonn',
            'Firstname': 'Wick',
            'Birthdate': '2003-10-24',
            'Nickname': '',
        }
    )
    user_data['person'].append(
        {
            'Surname': 'Linda',
            'Firstname': 'Brock',
            'Birthdate': '2003-9-21',
            'Nickname': 'Ichirooo12',
        }
    )
    user_data['person'].append(
        {
            'Surname': 'Nate',
            'Firstname': 'Wick',
            'Birthdate': '2003-10-1',
            'Nickname': 'GooSayaka''',
        }
    )

    with open('data_client.json', 'w') as file:
        json.dump(user_data, file)


if __name__ == "__main__":
    # create_datafile()
    person_list = []
    with open('data_client.json') as datafile:
        data = json.load(datafile)
        for user in data['person']:
            person = Person(user['Surname'], user['Firstname'], user['Birthdate'], user['Nickname'])
            person_list.append(person)

    modifier('extend_data_client.json', person_list)
