class Buffer:
    __MAX_SEQUENCE_LENGTH = 5

    def __init__(self):
        self.__sequence = []
        self.__sequence_sum = []

    def add(self, *args):
        for item in args:
            self.__sequence.append(item)
        if len(self.__sequence) > 5:
            for sum_item in self.sum_sequence:
                self.__sequence_sum.append(sum_item)
        return f'Elem sum:{self.__sequence_sum}'

    def get_current_part(self):
        return f"Sequence: {self.__sequence}"

    @property
    def sum_sequence(self):
        while len(self.__sequence) >= self.__MAX_SEQUENCE_LENGTH:
            sum_sequence = 0
            for i in range(5):
                sum_sequence += self.__sequence.pop(0)
            yield sum_sequence
