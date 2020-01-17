# Python Program for Sum of squares of first n natural numbers
# formulae = (n * (n+1) * (2n +1))/6

num = int(input('Enter the value of \'n\' : '))
result = (num * (num + 1) * (2 * num + 1)//6)

for i in range(1, num + 1):
    if i == num:
        print(f'{i ** 2} = {result}', end=' ')
    else:
        print(f'{i**2} + ', end=' ')


