# Python | Find all close matches of input string from a list

import difflib

try:
    user_input = []
    size = int(input('Enter the size of list : '))
    for index in range(size):
        while True:
            value = input(f'Enter {index + 1} element : ')
            if value==0 or value:
                user_input.append(value)
                break
            else:
                print('Invalid value. Try again')
    pattern = input('Enter the pattern : ')
    result = difflib.get_close_matches(pattern, user_input)
    print(f'{user_input} with pattern {pattern} returns : {result}')

except ValueError:
    print('Invalid Input')
