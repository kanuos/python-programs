# Python program to find N largest elements in a list


def find_n_largest_method_1(array, n):
    copy_array = [x for x in array]
    resultant_list = []
    for _ in range(n):
        current_max = max(copy_array)
        resultant_list.append(current_max)
        copy_array.remove(current_max)
    return resultant_list


def find_n_largest_method_2(array, n):
    copy_array = [x for x in array]
    copy_array.sort(reverse=True)
    return copy_array[:n]


try:
    num = int(input('Enter the number of elements : '))
    user_list = []
    for index in range(num):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value ==0 or value:
                user_list.append(value)
                break
            else:
                print('Please enter valid input')
    print('-'*70)
    N = int(input('Enter the value of "N" : '))
    if N > num:
        print('N cannot be greater than the size of the list')
    else:
        print('Calculated using Method 1')
        print(f'The largest {N} numbers '
              f'are {find_n_largest_method_1(user_list, N)}')
        print('-'*80)
        print('Calculated using Method 2')
        print(f'The largest {N} numbers '
              f'are {find_n_largest_method_2(user_list, N)}')
except ValueError:
    print('Invalid Value for the number of elements')