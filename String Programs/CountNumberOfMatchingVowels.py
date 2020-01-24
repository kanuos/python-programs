# Python program to count number of vowels using sets in given string


def count_vowels(string):
    vowel_count = 0
    for char in string:
        temp = char.lower()
        if temp == 'a' or temp == 'e' or temp == 'i' or temp =='o' or temp == 'u':
            vowel_count += 1
    return vowel_count


user_string = input('Enter the string : ')
result = count_vowels(user_string)
if result:
    print(f'No. of vowels : {result}')
else:
    print(f'No vowels in {user_string}')