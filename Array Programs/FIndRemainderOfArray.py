# Find reminder of array multiplication divided by n
# EXAMPLE :
# Input : arr[] = {100, 10, 5, 25, 35, 14},
#             n = 11
# Output : 9
# 100 x 10 x 5 x 25 x 35 x 14 = 61250000 % 11 = 9

from functools import reduce

try:
    length_of_list = int(input('Enter the number of elements in the list : '))
    user_array =  []
    for i in range(length_of_list):
        while True:
            value = int(input(f'Enter the {i + 1} element : '))
            if value:
                user_array.append(value)
                break
            else:
                print('Please enter valid input')

    divisor = int(input('Enter the dividing number : '))
    if divisor:
        # step 1: reduce the list
        reduced = reduce(lambda acc, cur: acc * cur, user_array, 1)
        # step 2: divide by divisor
        result = reduced % divisor
        print(f'{reduced} when divided by {divisor} leaves a quotient : {result}')
    else:
        print('Invalid Divisor. Quitting')
except ValueError:
    print('Invalid Input')

