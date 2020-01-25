# Python | Check if a given string is binary string or not

try:
    number = input('Enter the string : ')
    print(f'{number} is binary : {int(number, 2)}')
except ValueError:
    print('Not a binary number')