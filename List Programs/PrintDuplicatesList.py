# Python | Program to print duplicates from a list of integers


def duplicate_array(array):
    duplicates = []
    for item in array:
        if array.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
    return duplicates


try:
    user_input = []
    size = int(input('Enter the size of list : '))
    for index in range(size):
        while True:
            value = int(input(f'Enter {index + 1} element : '))
            if value == 0 or value:
                user_input.append(value)
                break
            else:
                print('Please try again with valid data')
    print(f'{user_input} has {duplicate_array(user_input)}')

except ValueError:
    print('Invalid Input')
