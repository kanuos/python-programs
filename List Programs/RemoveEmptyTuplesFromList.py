# Python | Remove empty tuples from a list

try:
    user_list = []
    size = int(input('Enter the size of the list : '))
    for index in range(size):
        user_list.append(tuple(input(f'Enter {index+1} element : ')))
    result_list = [x for x in user_list if x]
    print(f'{user_list} ==> {result_list}')
except ValueError:
    print('Size of list has to be number')
