# Given an int array length 2, return True if it contains a 2 or a 3.


def has23(array):
    result = 2 in array or 3 in array
    print(f"has23({array}) -> {result}")


has23([2, 5])
has23([4, 3])
has23([4, 5])
