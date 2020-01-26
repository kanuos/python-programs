# Python dictionary with keys having multiple inputs

try:
    while True:
        x = int(input('Enter the value of X : '))
        y = int(input('Enter the value of y : '))
        my_input = {
            '(x+y)(x+y)': (x + y) ** 2,
            '(x-y)(x-y)': (x - y) ** 2,
            '(x+y)(x+y)(x+y)': (x + y)**3,
            '(x+y)(x-y)': x**2 - y**2,
        }
        for k, v in my_input.items():
            print(f'{k} = {v}')
        print('Press "q" to quit.')
        command = input('Enter your command : ')
        if command.lower() == 'q':
            print('Quitting')
            break
except ValueError:
    print('Invalid values of x, y, z')
