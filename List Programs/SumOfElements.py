# Python program to find sum of elements in list

try:
    size = int(input('Enter the size of the list : '))
    user_list = []

    for index in range(size):
        while True:
            value = int(input(f'Enter the {index + 1} element : '))
            if value:
                user_list.append(value)
                break
            else:
                print('Value cannot be empty')

    print(f'The sum of {user_list} is {sum(user_list)}')
except ValueError:
    print('Invalid Input')
