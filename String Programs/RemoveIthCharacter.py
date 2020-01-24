# Ways to remove i’th character from string in Python
import os


def remove_i_char(string, i):
    char_list = list(string)
    char_list.remove(char_list[i])
    return ''.join(char_list)


user_string = input('Enter the string : ')
os.system('cls')
print(f'{user_string} has {len(user_string)} characters')
index = int(input('Enter the index to be removed : ')) - 1
if len(user_string) > index >= 0:
    print(f'Output = {remove_i_char(user_string, index)}')
    print(f'Element removed = {user_string[index]}')
else:
    print(f'{index} out of bound for string')
