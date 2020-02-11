# Given 3 int values, a b c, return their sum. However, if one of the values is the same as
# another of the values, it does not count towards the sum.


def lone_sum(a, b, c):
    if a != b and a != c and b != c:
        result = a + b + c
    else:
        if a == b and a != c:
            result = c
        elif b == c and a != c:
            result = a
        elif a == b == c:
            result = 0
        else:
            result = b
    print(f"lone_sum({a}, {b}, {c}) -> {result}")


lone_sum(1, 2, 3)
lone_sum(3, 2, 3)
lone_sum(3, 3, 3)