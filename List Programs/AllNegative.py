# Python program to print all positive numbers in a range

try:
    print(' Program to find all negative numbers in a range')
    start = int(input('Enter the "FROM" value : '))
    end = int(input('Enter the "TO" value : '))
    if end >= start:
        print(f'All the NEGATIVE numbers from {start} to {end} : ')
        for item in range(start, end + 1):
            if item < 0:
                print(item, end=',')
    else:
        print(f'All the NEGATIVE numbers from {end} to {start} : ')
        for item in range(start, end - 1, -1):
            if item < 0:
                print(item, end=',')
except ValueError:
    print('Invalid Input')
