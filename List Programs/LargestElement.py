# Python program to find largest number in a list

try:
    num = int(input('Enter the number of elements : '))
    user_list = []
    for index in range(num):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value ==0 or value:
                user_list.append(value)
                break
            else:
                print('Please enter valid input')
    print('-'*70)
    print(f'The largest of {user_list} is {max(user_list)}')
except ValueError:
    print('Invalid Value for the number of elements')