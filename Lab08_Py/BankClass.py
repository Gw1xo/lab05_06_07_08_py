import decimal


class Bank:
    def __init__(self, balance: decimal):
        self.__balance = balance

    def add_to_balance(self, funds: decimal):
        self.__balance += funds
        return 'Funding was successful'

    def withdrawal(self, funds: decimal):
        if self.__balance < funds:
            return "Insufficient funds to withdraw"
        self.__balance -= funds
        return "The withdrawal was successful"

    def check_balance(self):
        return f'The amount of funds on your balance is {self.__balance}'
