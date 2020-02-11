# Return the number of times that the string "hi" appears anywhere in the given string.


def count_hi(string):
    print(f"count_hi('{string}') -> {string.count('hi')}")


count_hi('abc hi ho')
count_hi('ABChi hi')
count_hi('hihi')
