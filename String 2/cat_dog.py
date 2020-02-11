# Return True if the string "cat" and "dog" appear the same number of times in the given string.


def cat_dog(string):
    result = True if string.count('cat') == string.count('dog') else False
    print(f"cat_dog('{string}') -> {result}")


cat_dog('catdog')
cat_dog('catcat')
cat_dog('1cat1cadodog')