# We want to make a row of bricks that is goal inches long. We have a number of small bricks
# (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal
# by choosing from the given bricks.


def make_bricks(small, big, goal):
    big *= 5
    result = False
    if goal == big or goal == small or goal % (small + big) == 0:
        result = True
    print(f"make_bricks({small}, {big}, {goal}) -> {result}")


make_bricks(3, 1, 8)
make_bricks(3, 1, 9)
make_bricks(3, 2, 10)