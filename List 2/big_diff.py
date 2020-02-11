# Given an array length 1 or more of ints, return the difference between the largest and smallest
# values in the array.


def big_diff(array):
    result = max(array) - min(array)
    print(f"big_diff({array}) -> {result}")


big_diff([10, 3, 5, 6])
big_diff([7, 2, 10, 9])
big_diff([2, 10, 7, 2])
