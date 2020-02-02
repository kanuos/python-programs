# Python counter and dictionary intersection example (Make a string using deletion and rearrangement)

from collections import Counter

try:
    s1 = input('Enter the string you want to create : ')
    s2 = input('Enter the characters to choose from : ')

    dict_from_s1 = Counter(s1)
    dict_from_s2 = Counter(s2)

    result = dict_from_s1 & dict_from_s2

    print('Possible') if result else print(' Not Possible')

except ValueError:
    print('Invalid Input')