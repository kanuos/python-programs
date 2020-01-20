# Python program to interchange first and last elements in a list


def interchange_elements(input_list):
    array = [x for x in input_list]
    first_element = array[0]
    array[0] = array[-1]
    array[-1] = first_element
    return array


try:
    user_list = []
    num = int(input('Enter the number of elements : '))
    for i in range(num):
        while True:
            value = input(f'Enter the {i + 1} value : ')
            if value:
                user_list.append(value)
                break
            else:
                print('Please enter valid input')
    print(f'The original list : {user_list}')
    print(f'The modified list : {interchange_elements(user_list)}')
except ValueError:
    print('Number of elements must be a number')