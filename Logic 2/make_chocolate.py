# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars
# (5 kilos each). Return the number of small bars to use, assuming we always use big bars before
# small bars. Return -1 if it can't be done.


def make_chocolate(small, big, goal):
    big *= 5
    number_of_smalls = small - (goal - big)
    print(f"make_chocolate({small}, {big}, {goal}) -> {number_of_smalls}")


make_chocolate(4, 1, 9)
make_chocolate(4, 1, 10)
make_chocolate(4, 1, 7)