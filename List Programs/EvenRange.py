# Python program to print all even numbers in a range


def even_numbers(start, end):
    return [x for x in range(start, end) if x%2 == 0]


try:
    print('\t Program to find even numbers in a range')
    start = int(input('Enter the "FROM" value : '))
    end = int(input('Enter the "TO" value : '))
    if end >= start:
        print(f'The even numbers from {start} to {end} are : \n {even_numbers(start, end+1)}')
    else:
        print('Invalid Range')
except ValueError:
    print('Invalid Input')
