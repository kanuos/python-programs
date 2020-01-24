# Generating random strings until a given string is generated
import random, time


def generate_random_string(input_string):
    size = len(input_string)
    start = time.time()
    iterator_count = 0
    all_characters = []
    print('Guessing...')
    for item in range(97, 123):
        all_characters.append(chr(item))
    while True:
        guess = random.choices(all_characters, k=size)
        iterator_count += 1
        guess_word = ''.join(guess)
        if guess_word == input_string:
            print('Guessed')
            break
    end = time.time()
    return {
        'duration': end - start,
        'attempts': iterator_count
    }


user_string = input('Enter a lowercase string : ')
user_string = user_string.lower()
result = generate_random_string(user_string)
print(f'Your word : {user_string} was guessed in {result["duration"]} seconds and in {result["attempts"]} attempts')
