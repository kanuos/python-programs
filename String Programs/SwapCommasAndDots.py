# Python | Swap commas and dots in a String


def swap_commas_dots(string):
    string_list = []
    for char in string:
        if char == ',':
            string_list.append('.')
        elif char == '.':
            string_list.append(',')
        else:
            string_list.append(char)
    return ''.join(string_list)


try:
    user_string = input('Enter the string : ')
    print(f'{user_string} on comma-dot swapping returns : ')
    print(swap_commas_dots(user_string))

except ValueError:
    print('Invalid Input')

