# Python program to count Even and Odd numbers in a List


def count_odd_even(array):
    odd_counter , even_counter = 0, 0
    for item in array:
        if item % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    return {
        'odd':odd_counter,
        'even':even_counter
    }


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
    print(f'Size of input list : {len(user_list)}')
    print(f'Number of Evens : {count_odd_even(user_list)["even"]}')
    print(f'Number of Odds : {count_odd_even(user_list)["odd"]}')

except ValueError:
    print('Invalid Input')
