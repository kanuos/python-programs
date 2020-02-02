# Python | Check order of character in string

try:
    string = input('Enter the string : ')
    sub_string = input('Enter the sub string you want to check : ')

    if sub_string in string:
        print(f'{sub_string} is present in {string} at {string.index(sub_string)}')
    else:
        print(f'{sub_string} is not present in {string}.')

except ValueError:
    print('Input error')
