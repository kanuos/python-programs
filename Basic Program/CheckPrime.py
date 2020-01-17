# Python program to check whether a number is Prime or not


def is_prime(num):
    return num % 2 == 0


number = int(input('Enter the number to check whether it is prime or not: '))
print(f'{number} is a Prime Number : {is_prime(number)}')
