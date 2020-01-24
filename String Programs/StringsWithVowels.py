# Python | Program to accept the strings which contains all vowels


def screen_vowel_word(string):
    word_list = string.split(' ')
    vowel_words = []
    for item in word_list:
        if len(item) < 5:
            break
        else:
            temp = item.lower()
            if 'a' in temp and 'e' in temp and \
                    'i' in temp and 'o' in temp and 'u' in temp:
                vowel_words.append(item)
    return vowel_words


user_string = input('Enter the sentence : ')
print(f'The all-vowel-words are :')
print(screen_vowel_word(user_string))

