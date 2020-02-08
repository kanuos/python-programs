# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
import math


def diff21(num):
    if num > 21:
        return round(2 * math.fabs(num - 21))
    return round(math.fabs(21-num))


print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(25))
