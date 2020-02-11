# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True,
# in which case return True if the number is less or equal to 1, or greater or equal to 10.


def in1to10(n, outside_mode):
    if outside_mode:
        jimbo = True if n >= 10 or n <= 1 else False
    else:
        jimbo = 10 >= n >= 1
    print(f"in1to10({n}, {outside_mode}) -> {jimbo}")


in1to10(5, False)
in1to10(11, False)
in1to10(11, True)
