# Python Program to check if a given number is Fibonacci number


def check_fibonacci(number):
    first, second = 0, 1
    third = first + second
    fibonacci = [first, second]
    while third < number:
        third = first + second
        first = second
        second = third
        fibonacci.append(third)
    print(fibonacci)
    if number in fibonacci:
        return 'a Fibonacci number'
    return 'Not a Fibonacci number'


print('Check whether a number is in the Fibonacci sequence.')
num = int(input('Enter the number: '))
print(f'{num} is {check_fibonacci(num)}')
