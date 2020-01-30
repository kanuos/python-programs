# Python Dictionary to find mirror characters in a string
#65 A B C D E F G H I J K L M 77
#90 Z Y X W V U T S R Q P O N 78
import os


def calculate_mirror_character(char):
    alphabet = [chr(x) for x in range(65, 91)]
    if char.islower():
        char = char.upper()
    if char.isalpha():
        if 'M' >= char >= 'A':
            position = (alphabet.index(char)) + 1
            return alphabet[-1 * position]
        position = 25 - alphabet.index(char)
        return alphabet[position]
    return char


def generate_mirror(string):
    string_list = list(string)
    for index in range(len(string)):
        string_list[index] = calculate_mirror_character(string_list[index])
    return ''.join(string_list)


try:
    user_input = input('Enter a word : ')
    result = generate_mirror(user_input)
    os.system('cls')
    print('''
    A B C D E F G H I J K L M
    Z Y X W V U T S R Q P O N
    ''')
    print(f'The mirror of "{user_input}" : "{result}"')
except ValueError:
    print('Invalid Input')
