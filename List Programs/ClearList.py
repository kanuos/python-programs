# Different ways to clear a list in Python

try:
    size = int(input('Enter the size of the list : '))
    user_list = []

    for index in range(size):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value:
                user_list.append(value)
                break
            else:
                print('Value cannot be empty')

    print(f'Your entered list : {user_list}')
    user_list.clear()
    print(f'Your list after clearing : {user_list}')

except ValueError:
    print('Invalid Input')
