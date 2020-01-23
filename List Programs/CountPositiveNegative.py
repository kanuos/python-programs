# Python program to count positive and negative numbers

try:
    print(' Program to count positive and negative numbers in a list')
    size = int(input('Enter the size of the list : '))
    user_list = []
    positive, negative = 0, 0
    for index in range(size):
        while True:
            value = int(input(f'Enter the {index + 1} element : '))
            if value == 0 or value:
                user_list.append(value)
                break
            else:
                print('Please try again later')

    for item in user_list:
        if item >= 0:
            positive += 1
        else:
            negative += 1
    print(f'{user_list} has {positive} positives and '
          f'{negative} negatives')
except ValueError:
    print('Invalid Input')
