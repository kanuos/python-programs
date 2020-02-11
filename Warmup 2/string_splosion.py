# Given a non-empty string like "Code" return a string like "CCoCodCode".
import os


def string_splosion(word):
    index = 0
    result = ""
    while index <= len(word):
        result += word[:index]
        index += 1
    return result


try:
    count = 0
    while True:
        user = input('Enter the word (:q to quit): ')
        if user == ":q":
            print(f'Quitting, after {count} times')
            break
        print(string_splosion(user))
        count += 1
        os.system('CLS')
except ValueError:
    print("Invalid Input")