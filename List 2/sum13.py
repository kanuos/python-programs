# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately
# after a 13 also do not count.


def sum13(array):
    result = [x for x in array if x != 13]
    print(f"sum13({array}) -> {sum(result)}")


sum13([1, 2, 2, 1])
sum13([1, 1])
sum13([1, 2, 2, 1, 13])
