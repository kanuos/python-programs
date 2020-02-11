# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
import math


def make_pi(num):
    pi_list = list(str(math.pi))
    pi_list.remove('.')
    print(f"make_pi({num}) -> {pi_list[:num]}")


print("The value of PI : ", str(math.pi))
make_pi(5)
make_pi(10)
make_pi(3)