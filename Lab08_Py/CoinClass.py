import random


class Coin:

    def __init__(self):
        self.__sideup = ('heads', 'tails')

    def toss(self):
        return self.__sideup[random.randint(0, 1)]
