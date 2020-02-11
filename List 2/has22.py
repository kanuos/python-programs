# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


def has22(array):
    result = False
    for i in range(len(array) - 1):
        if array[i] == 2 and array[i+1] == 2:
            result = True
            break
    print(f"has22({array}) -> {result}")


has22([1, 2, 2])
has22([1, 2, 1, 2])
has22([2, 1, 2])
