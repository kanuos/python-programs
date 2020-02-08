# Given two int values, return their sum. Unless the two values are the same,
# then return double their sum.


def sum_double(first, second):
    return first + second if first != second else (first + second) * 2


print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))
