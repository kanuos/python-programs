# Python | Reversing a List

try:
    num = int(input('Enter the number of elements : '))
    user_list = []
    for index in range(num):
        while True:
            value = int(input(f'Enter the {index+1} element : '))
            if value == 0 or value:
                user_list.append(value)
                break
            else:
                print('Please enter numbers')
    print('-'*70)
    print(f'Original List : {user_list}')
    print(f'The Reversed List : {user_list[::-1]}')
except ValueError:
    print('Invalid Input')
