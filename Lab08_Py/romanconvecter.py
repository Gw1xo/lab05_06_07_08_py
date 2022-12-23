class Roman:
    coding = zip(
        [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
        ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    )

    coding_dict = {
        'M': 1000,
        'D': 400,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }


class IntToRoman(Roman):
    def dec_to_roman(self, num):
        if num <= 0 or num >= 4000 or int(num) != num:
            raise ValueError('Input should be an integer between 1 and 3999')
        result = []
        for d, r in self.coding:
            while num >= d:
                result.append(r)
                num -= d
        return ''.join(result)


class RomanToInt(Roman):
    def roman_to_dec(self, roman_num):
        roman_num: str
        roman_list = list(roman_num)

        stack = []

        for x in roman_list:
            stack.append(self.coding_dict[x])

        number = 0
        while stack:
            if stack[0] == max(stack):
                number += stack.pop(0)
            else:
                number -= stack.pop(0)

        return number
