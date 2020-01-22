# Python | Ways to check if element exists in list

try:
    print('Program to Check whether a number is present in a range')
    start = int(input('Enter the starting number of the range : '))
    end = int(input('Enter the ending number of the range : '))

    if start > end:
        print('Invalid range')
    else:
        number_to_check = int(input('Enter the number to check : '))
        if number_to_check in range(start, end):
            print(f'{number_to_check} is present in the range')
        else:
            print(f'{number_to_check} is NOT present in the range')

except ValueError:
    print('Invalid Input')
