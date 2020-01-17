# Python Program for Fibonacci numbers


def fibonacci(number):
    first, second, third = 0, 1, 1
    fibonacci_list = [first, second]
    if number <= 1:
        return [0]
    elif number <= 2:
        return fibonacci_list
    for _ in range(number - 2):
        third = first + second
        first = second
        second = third
        fibonacci_list.append(third)
    return fibonacci_list


print('Generate fibonacci numbers')
num = int(input('Enter the number: '))
print(fibonacci(num))
