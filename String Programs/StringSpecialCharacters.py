# Python | Program to check if a string contains any special character
# 33 -47
# Code 58-64
# Code 91-96
# Code 123 - 127


def check_special(string):
    flag = False
    for char in string:
        ascii_char = ord(char)
        if 47 >= ascii_char >= 33 or 64 >= ascii_char >= 58 \
                or 96 >= ascii_char >= 91 or 127 >= ascii_char >= 123:
            flag = True
            break
    return flag


user_string = input('Enter the string : ')
result = check_special(user_string)
if result:
    print(f'{user_string} is not accepted')
else:
    print(f'{user_string} is accepted')
