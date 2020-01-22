# Python program to find second largest number in a list

try:
    size = int(input('Enter the size of the list : '))
    user_list = []
    result = None
    for index in range(size):
        while True:
            value = int(input(f'Enter the {index + 1} element : '))
            if value:
                user_list.append(value)
                break
            else:
                print('Value cannot be empty')

    working_list = [x for x in user_list]

    working_list.remove(max(working_list))
    result = max(working_list)

    print(f'The 2nd largest number of {user_list} is {result}')
except ValueError:
    print('Invalid Input')
