# Python program to print even numbers in a list


def even_numbers(array):
    return [x for x in array if x%2 == 0]


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
    print(f'The even numbers of the list : {even_numbers(user_list)}')
except ValueError:
    print('Invalid Input')