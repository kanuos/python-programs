# Python program to find the sum of all items in a dictionary
import os


def sum_dictionary(dictionary):
    return sum(dictionary.values())


try:
    user_dict = {}
    size = int(input('Enter the size of the dictionary : '))
    for index in range(size):
        while True:
            key = input(f'Enter the {index + 1} key : ')
            value = int(input(f'Enter the {index + 1} value : '))
            print('-'*70)
            if key == 0 or key and value == 0 or value:
                user_dict[key] = value
                break
            else:
                print('Please enter valid Key and Value')
    os.system('cls')
    print(f'Input : {user_dict}')
    print(f'Output : {sum_dictionary(user_dict)}')

except ValueError:
    print('Input cannot be empty.')
