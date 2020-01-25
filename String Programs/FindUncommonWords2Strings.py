# Python program to find uncommon words from two Strings


def uncommon_words(string1, string2):
    set_a = set(string1.split(' '))
    set_b = set(string2.split(' '))
    words = list(set_a.difference(set_b))
    words.extend(list(set_b.difference(set_a)))
    return words


try:
    first_string = input('Enter the first string : ')
    second_string = input('Enter the second string : ')
    word_list = uncommon_words(first_string, second_string)
    print(word_list)
except ValueError:
    print('Invalid Input')
