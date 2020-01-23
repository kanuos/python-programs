# Break a list into chunks of size N in Python
# Insert m number of elements in list
# return r number of arrays of N size
import math


def user_input(s):
    resultant = []
    try:
        for index in range(s):
            while True:
                value = int(input(f'Enter {index+1} element : '))
                if value == 0 or value:
                    resultant.append(value)
                    break
                else:
                    print('Please enter valid elements')
        return resultant
    except ValueError:
        print('Invalid input')


def divide_in_chunks(array, n):
    resultant = []
    loop_count = math.ceil(len(array) // n)
    start, end = 0, n
    while loop_count >= 0:
        temp_array = array[start: end]
        start = end
        end = end + n
        loop_count -= 1
        if len(temp_array):
            resultant.append(temp_array)
    print(f'{array} when divided into {n} sized chunks :')
    print(resultant)


try:
    size = int(input('Enter the size of the list : '))
    user_list = user_input(size)
    chunk_size = int(input('Enter the size of the chunk : '))
    divide_in_chunks(user_list, chunk_size)
except ValueError:
    print('Size of list has to be an integer')