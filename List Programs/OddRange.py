# Python program to print all odd numbers in a range


def odd_numbers(beginning, finish):
    return [x for x in range(beginning, finish) if x % 2 != 0]


try:
    print('\t Program to find even numbers in a range')
    start = int(input('Enter the "FROM" value : '))
    end = int(input('Enter the "TO" value : '))
    if end >= start:
        print(f'The odd numbers from {start} to {end} are : \n {odd_numbers(start, end+1)}')
    else:
        print('Invalid Range')
except ValueError:
    print('Invalid Input')
