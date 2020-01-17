# Python Program to check if given array is Monotonic

monotonous = {
    'status' : False,
    'monotonous_inc' : False,
    'monotonous_dec': False
}
input_list = []

num = int(input('Enter the number of elements : '))
# filling input list
for index in range(num):
    input_list.append(float(input(f'Enter list[{index}] : ')))

# sort the list both ways
sorted_list = sorted(input_list)
sorted_list_reverse = sorted(input_list, reverse=True)

if sorted_list == input_list:
    monotonous["status"] = True
    monotonous["monotonous_inc"] = True
elif sorted_list_reverse == input_list:
    monotonous["status"] = True
    monotonous["monotonous_dec"] = True

result = ''
if monotonous["status"]:
    if monotonous["monotonous_dec"]:
        result = 'Monotone Decreasing'
    else:
        result = 'Monotone Increasing'
else:
    result = 'Not Monotonic'

print('-'*60)
print(f'{input_list} is {result}')
