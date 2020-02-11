# Given 2 ints, a and b, return their sum. However, sums in the range 10..19
# inclusive, are forbidden, so in that case just return 20.


def sorta_sum(a, b):
    result = 20 if 19 >= a + b >= 10 else a + b
    print(f"sorta_sum({a}, {b}) -> {result}")


sorta_sum(3, 4)
sorta_sum(9, 4)
sorta_sum(10, 11)
