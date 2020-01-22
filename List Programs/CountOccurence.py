# Python | Count occurrences of an element in a list

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
    char = input('Enter the element to count occurrence : ')
    char_count = user_list.count(char)
    if char_count == 0:
        print(f'{char} is not present in {user_list}')
    else:
        print(f'{char} is present in {user_list} {char_count}times')
except ValueError:
    print('Invalid Input')
