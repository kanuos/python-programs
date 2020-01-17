# Python Program for factorial of a number


def factorial(num):
    result = 1
    if num <= 0:
        return 0
    while num >= 1:
        result *= num
        num -= 1
    return result


number = int(input('Enter the number : '))
print(f'The factorial of {number} is {factorial(number)}')
