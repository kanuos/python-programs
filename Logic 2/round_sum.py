# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit
# is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if
# its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum
# of their rounded values. To avoid code repetition, write a separate helper "def round10(num):"
# and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().


def round10(int):
    if int < 10 :
        if int > 5:
            return 10
        return 0
    else:
        int %= 10
        if int > 5:
            return 20
        return 10


def round_sum(a , b, c):
    print(f"round_sum({a}, {b}, {c}) -> {round10(a) + round10(b) + round10(c)}")


round_sum(16, 17, 18)
round_sum(12, 13, 14)
round_sum(6, 4, 4)