class User:
    def __init__(self, first_name: str, last_name: str, email: str, nickname: str, news_agree: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.nickname = nickname
        self.news_agree = news_agree

    login_attempts = 0

    @property
    def describe_user(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def greeting_user(self):
        return f'Hello,{self.describe_user}'

    def increment_logit_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
