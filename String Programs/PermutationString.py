# Python | Permutation of a given string using inbuilt function
from itertools import permutations

user_string = input('Enter the string : ')
print('Permutation strings : ')
perms = list(permutations(user_string))

for item in perms:
    print(''.join(item))

