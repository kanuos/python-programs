# Find length of a string in python (4 ways)


def find_length_method_1(string):
    return len(string)


def find_length_method_2(string):
    count = 0
    for _ in string:
        count += 1
    return count


user_string = input('Enter the string : ')
print(f'{user_string} is {find_length_method_1(user_string)} chars long')
print(f'{user_string} is {find_length_method_2(user_string)} chars long')
