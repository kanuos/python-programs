# Python Program for simple interest


def calculate_simple_interest(p, t, r):
    no_of_months = 12
    return (p * t * r)/(100 * no_of_months)


print('-'*50)
principal = float(input('Enter the principal amount : '))
time = int(input('Enter the period (months) : '))
rate = float(input('Enter the rate of interest : '))

print('-'*50)
print(
    f'The simple interest is : '
    f'{calculate_simple_interest(principal, time, rate)}'
)
