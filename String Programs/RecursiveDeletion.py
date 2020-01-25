# String slicing in Python to check if a string can become empty by recursive deletion


def recursive_deletion(string, sub_str):
    for _ in range(len(string)):
        if sub_str in string:
            string = string.replace(sub_str, '')
        else:
            break
    return len(string)


user_string = input('String : ')
user_sub_string = input('Sub-String : ')

result = recursive_deletion(user_string, user_sub_string)

if not result:
    print(f'{user_string} can be deleted recursively by {user_sub_string}')
else:
    print(f'{user_string} can NOT be deleted recursively by {user_sub_string}')