# Python Program for cube sum of first n natural numbers
# formula = (n * (n+1))/2

num = int(input('Enter the value of \'n\' : '))
result = (num * (num + 1)) // 2

for i in range(1, num + 1):
    if i == num:
        print(f'{i} = {result}', end=' ')
    else:
        print(f'{i} + ', end=' ')
