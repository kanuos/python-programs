# Python program to print even length words in a string


def even_length(string):
    word_list = string.split(' ')
    my_dict = {}
    for item in word_list:
        if len(item) % 2 == 0:
            my_dict[item] = len(item)
    return my_dict


user_string = input('Enter the string : ')
print(f'The even length words of {user_string} are : ')
print(even_length(user_string))
