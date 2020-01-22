# Remove multiple elements from a list in Python

try:
    size = int(input('Enter the size of the list : '))
    user_list = []
    remove_list = []
    for index in range(size):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value:
                user_list.append(value)
                break
            else:
                print('Value cannot be empty')
    size = int(input('How many Elements to remove ? '))

    for index in range(size):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value:
                remove_list.append(value)
                break
            else:
                print('Value cannot be empty')

    print('-'*70)

    print(f'{user_list}.remove_multiple({remove_list}) returns  '
          f'{list(set(user_list).difference(set(remove_list)))}')
except ValueError:
    print('Invalid Input')
