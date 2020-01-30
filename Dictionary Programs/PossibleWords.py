# Possible Words using given characters in Python


def evaluate_possible_words(word_dict, char_list):
    possible = []
    for word in word_dict:
        flag = True
        for char in word:
            if char not in char_list:
                flag = False
                break
        if flag:
            possible.append(word)
    return possible


def user_input(num, category):
    store = []
    for index in range(num):
        while True:
            value = input(f'Enter the {index + 1} {category} : ')
            if value == 0 or value:
                store.append(value)
                break
            else:
                print(f'Invalid value for {index + 1} {category}')
    print('*'*80)
    return store


try:
    size = int(input('Enter the size of the dictionary : '))
    user_word = user_input(size, 'word')
    user_characters = user_input(size, 'characters')
    result = evaluate_possible_words(user_word, user_characters)
    print(f'The possible words are : {result}')
except ValueError:
    print('Invalid Input')