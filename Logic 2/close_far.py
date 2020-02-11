# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
# while the other is "far", differing from both other values by 2 or more.


def close_far(a, b, c):
    result = False
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 and abs(b - c) >= 2:
            result = True
    elif abs(c - a) <= 1:
        if abs(b - a) >= 2 and abs(b - c) >=2:
            result = True
    else:
        result = False
    print(f"close_far({a}, {b}, {c}) -> {result}")


close_far(1, 2, 10)
close_far(1, 2, 3)
close_far(4, 1, 3)