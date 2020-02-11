# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the
# range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens.
# Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed
# for the teen rule


def fix_teen(num):
    if 13 <= num <= 19:
        return 0
    else:
        return num


def no_teen_sum(a, b, c):
    result = fix_teen(a) + fix_teen(b) + fix_teen(c)
    print(f"no_teen_sum({a}, {b}, {c}) -> {result}")


no_teen_sum(1, 2, 3)
no_teen_sum(2, 13, 1)
no_teen_sum(2, 1, 14)
