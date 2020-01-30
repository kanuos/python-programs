# Python | Remove all duplicates words from a given sentence


def remove_duplicates(string):
    unique_words = []
    word_list = string.split(' ')
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)


try:
    sentence = input('Enter the sentence : ')
    if sentence == 0 or sentence:
        result = remove_duplicates(sentence)
        print(f'{sentence} without duplicate words : "{result}"')
except ValueError:
    print('Invalid String')