# Python | Check if a Substring is Present in a Given String


def check_substring(string, sub_string):
    return sub_string in string


user_string = input('Enter the original string : ')
user_sub_string = input('Enter the sub-string to check : ')

if check_substring(user_string, user_sub_string):
    print(f'{user_string} has {user_sub_string} at {user_string.index(user_sub_string) + 1}')
else:
    print(f'{user_string} does not have {user_sub_string}')

