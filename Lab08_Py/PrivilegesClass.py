from UserClass import User


class Privileges:
    privileges = [
        'Allowed to add message',
        'Allowed to delete users',
        'Allowed to ban users'
    ]

    @property
    def show_privileges(self):
        for privilege in self.privileges:
            yield privilege


class Admin(User, Privileges):
    def __init__(self, first_name: str, last_name: str, email: str, nickname: str, news_agree: bool):
        super().__init__(first_name, last_name, email, nickname, news_agree)