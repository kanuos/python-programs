# Python program to swap two elements in a list
import os


def swap_elements(array, first_index, second_index):
    temp_array = [x for x in array]
    temp_first = temp_array[first_index]
    temp_second = temp_array[second_index]
    temp_array[second_index] = temp_first
    temp_array[first_index] = temp_second
    return temp_array


try:
    user_input = []
    num = int(input('Enter the number of elements : '))
    for index in range(num):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value==0 or value:
                user_input.append(value)
                break
            else:
                print('Please enter a valid input')
    first = int(input('Enter the first index to swap : ')) - 1
    second = int(input('Enter the second index to swap : ')) - 1
    if first < num and second < num:
        os.system('cls')
        print(f'Original array : {user_input}')
        print('*'*70)
        print(f'Modified list : {swap_elements(user_input,first, second)}')
    else:
        print('Index out of bound error')
except ValueError:
    print('Invalid Input')