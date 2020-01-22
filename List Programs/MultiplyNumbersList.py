# Python | Multiply all numbers in the list
from functools import reduce
try:
    size = int(input('Enter the size of the list : '))
    user_list = []

    for index in range(size):
        while True:
            value = int(input(f'Enter the {index + 1} element : '))
            if value == 0 or value:
                user_list.append(value)
                break
            else:
                print('Value cannot be empty')

    product = reduce(lambda acc, cur: acc * cur, user_list, 1)
    print(f'The product of all numbers of {user_list} is {product}')
except ValueError:
    print('Invalid Input')
