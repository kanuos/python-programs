# Python program to check if a string is palindrome or not


def check_palindrome(string):
    temp_string = string[::-1]
    if temp_string == string:
        return True
    return False


user_string = input('Enter the string: ')
if check_palindrome(user_string):
    print(f'{user_string} is a palindrome string')
else:
    print(f'{user_string} is NOT a palindrome string')
