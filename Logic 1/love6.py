# The number 6 is a truly great number. Given two int values, a and b, return True
# if either one is 6. Or if their sum or difference is 6.


def love6(first, second):
    love = True if first == 6 or second == 6 or abs(first + second) == 6 or\
                   abs(first - second) == 6 else False
    print(f"love({first}, {second}) -> {love}")


love6(6, 4)
love6(4, 5)
love6(1, 5)