# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.


def pos_neg(first, second, negative):
    if negative:
        if first < 0 and second < 0:
            return True
        return False
    if (first < 0 and second > 0) or (first > 0 and second < 0):
        return True
    return False


print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
