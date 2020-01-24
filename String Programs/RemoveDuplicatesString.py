# Remove all duplicates from a given string in Python


def remove_duplicates(string):
    duplicates = []
    residual = [x for x in string]
    for char in string:
        if char not in duplicates:
            duplicates.append(char)
            residual.remove(char)
    return ''.join(duplicates)


user_string = input('Enter the string : ')
if user_string:
    result = remove_duplicates(user_string)
    print(f'Duplicates of {user_string} is : {result}')
else:
    print('Input cannot be empty')
