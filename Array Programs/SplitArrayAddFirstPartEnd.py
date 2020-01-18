# Python Program to Split the array
# and add the first part to the end


def split_and_switch(array, index):
    first_part = array[:index]
    last_part = array[index:]
    last_part.extend(first_part)
    return last_part


try:
    num = int(input('Enter the size of the list : '))
    user_list = []
    for i in range(num):
        while True:
            value = input(f'Enter the {i + 1} element : ')
            if value:
                user_list.append(value)
                break
            else:
                print('Please enter valid input')

    split_index = int(input('Enter the splitting index : '))
    if split_index:
        if split_index > num:
            print('The splitting index cannot be greater than the size of the lab')
        else:
            print('-'*50)
            print(split_and_switch(user_list, split_index))
    else:
        print('Enter valid splitting index')
except ValueError:
    print('Invalid Input')
