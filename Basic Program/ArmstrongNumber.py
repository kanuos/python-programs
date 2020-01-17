# Python Program to check Armstrong Number
# 153 = cube(1) + cube(5) + cube(3)


def is_armstrong_number(number):
    temp = number
    result = 0
    while temp > 0:
        first_digit = temp % 10
        result += first_digit**3
        temp //= 10
    return result == number


print('Armstrong Number')
print('-'*50)
num = int(input('Enter the number here : '))
output = 'Is Armstrong Number' if is_armstrong_number(num) is True else 'not an Armstrong number'
print(f'{num} is {output}')