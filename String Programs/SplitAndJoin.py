# Python program to split and join a string


def split_and_join(string, char):
    array = string.split(' ')
    join_list = char.join(array)
    return {
        'split': array,
        'join': join_list
    }


try:
    user_string = input('Enter the string : ')
    split_char = input('Enter the character you want to join with : ')
    result = split_and_join(user_string, split_char)
    print(f'{user_string} when split by {split_char}')
    print(f'Split list : {result["split"]}')
    print(f'Join list : {result["join"]}')

except ValueError:
    print('Invalid Input')
