# Generate all possible letter combinations for phone numbers

from itertools import product

def phone_letter_combinations():
    phone_numbers = {
        '1': [''],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
        '0': ['+'],
        '*': [''],
        '#': [''],
    }

    digits = list(input('Enter digits : '))

    # Creating a list of possible combinations
    combinations = list(map(list, product(*(phone_numbers[Values] for Values in digits))))

    # Adjusting outcome
    pool = ""

    # Making string instead list
    for element in combinations:
        cycles = 0
        for letter in element:
            pool += str(letter)
            cycles += 1
            if cycles % len(element) == 0:
                pool += ','

    output_li = pool.split(',')
    output_li.pop()

    return output_li

print(phone_letter_combinations())
