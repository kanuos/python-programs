# Given a string and a non-negative int n, return a larger string that is n copies of the original string.


def string_times(string, number):
    return string * number


try:
    word = input('Enter the word: ')
    num = int(input('Enter the times value : '))
    print(f" {word} * {num} : {string_times(word, num)}")
except ValueError:
    print('Invalid Input')
