# Python Program to find largest element in an array

num = int(input('Enter the number of elements in list : '))
input_list = []

for i in range(num):
    if i == 0:
        input_list.append(int(input(f'Enter the {i+1}st element : ')))
    elif i == 1:
        input_list.append(int(input(f'Enter the {i + 1}nd element : ')))
    elif i == 2:
        input_list.append(int(input(f'Enter the {i + 1}rd element : ')))
    else:
        input_list.append(int(input(f'Enter the {i + 1}th element : ')))

print('-'*60)
print(f'The largest of {input_list} is {max(input_list)}')
