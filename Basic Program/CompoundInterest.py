# Python Program for compound interest


def calculate_compound_interest(p,t,r,n):
    r = r/100
    amount = p * (1+r/n)**(n*t)
    return amount


print('-'*50)
principal = float(input('Enter the principal : '))
time = int(input('Enter the time period : '))
rate = float(input('Enter the rate of interest : '))
compounding_frequency = int(input('Enter compounding frequency in momths : '))
print('-'*50)
result = calculate_compound_interest(principal, time, rate, compounding_frequency)

print(f'Final amount {round(result,2)}')
