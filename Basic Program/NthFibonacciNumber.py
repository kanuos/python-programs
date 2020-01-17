# Python Program for n-th Fibonacci numbers


def fibonacci(number):
    first, second, third = 0, 1, 1
    fibonacci_list = [first, second]
    if number <= 1:
        return [0]
    for _ in range(number):
        third = first + second
        first = second
        second = third
        fibonacci_list.append(third)
    print(fibonacci_list[:-2])
    return fibonacci_list[-3]  # [0,1] already in list


print('n-th fibonacci numbers')
num = int(input('Enter the number: '))
print(f'The {num}-th fibonacci number is : {fibonacci(num)}')
