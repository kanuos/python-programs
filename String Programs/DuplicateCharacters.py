# Python Counter| Find all duplicate characters in string


def find_duplicate(string):
    duplicates = {}
    for char in string:
        if string.count(char) > 1:
            if char not in duplicates.keys():
                duplicates[char] = string.count(char)
    return duplicates


user_string = input('Input : ')
print(f'Output : {find_duplicate(user_string)}')
