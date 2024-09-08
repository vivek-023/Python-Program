class IntegerToRoman:
    def __init__(self):
        self.roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, num):
        result = ""
        for value, numeral in self.roman_numerals:
            while num >= value:
                result += numeral
                num -= value
        return result

def main():
    converter = IntegerToRoman()
    
    numbers = [3, 9, 58, 1994, 2023]
    
    print("Integer to Roman numeral conversion:")
    for number in numbers:
        roman_numeral = converter.int_to_roman(number)
        print(f"{number} -> {roman_numeral}")

if __name__ == "__main__":
    main()
