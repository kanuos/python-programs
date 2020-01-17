# Python program to print all Prime numbers in an Interval


def is_prime(n):
    return True if n % 2 == 0 else False


print('Print all the prime numbers within a range')
start = int(input('Enter the starting number: '))
end = int(input('Enter the ending number: '))

if start > end:
    print('Invalid Range.')
else:
    print('-'*50)
    print(f'Prime numbers from {start} to {end} ')
    for item in range(start, end+1):
        if is_prime(item):
            print(item, end=',')

