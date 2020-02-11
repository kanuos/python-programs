# Given a non-negative number "num", return True if num is within 2 of a multiple of 10.


def near_ten(num):
    remainder = num % 10
    result = True if remainder <= 2 or  abs(10 - remainder) <= 2 else False
    print(f"near_ten({num}) -> {result}")


near_ten(12)
near_ten(17)
near_ten(19)


