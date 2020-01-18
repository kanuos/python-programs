# Python Program for array rotation


def rotate_array(array, rotation_index):
    rotation_index -= 1
    new_arr = array[rotation_index:]
    new_arr.extend(array[:rotation_index])
    print(new_arr)

try:
    num = int(input('Enter the number of elements in the array: '))
    user_array = []
    for index in range(num):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value:
                user_array.append(value)
                break
            else:
                print('Enter valid input')
    pivot = int(input('Enter the index on which you want to rotate : '))

    if pivot > num:
        print('Pivot cannot be greater than length of list')
    else:
        rotate_array(user_array, pivot)
except ValueError:
    print('Invalid Input')
