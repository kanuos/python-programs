# Reverse words in a given String in Python


def reverse_words(string):
    words_list = string.split(' ')
    return ' '.join(words_list[::-1])


user_string = input('Enter the sentence : ')
print(f'"{user_string}" reversed is "{reverse_words(user_string)}" ')