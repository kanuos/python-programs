# Python program to print all positive numbers in a list

try:
    print(' Program to find all positive numbers in a list')
    size = int(input('Enter the size of the list : '))
    user_list = []
    for index in range(size):
        while True:
            value = int(input(f'Enter the {index + 1} element : '))
            if value == 0 or value:
                user_list.append(value)
                break
            else:
                print('Please try again later')
    print(f'The positive numbers of {user_list} are : ')
    for item in user_list:
        if item >= 0:
            print(item, end=',')
except ValueError:
    print('Invalid Input')
