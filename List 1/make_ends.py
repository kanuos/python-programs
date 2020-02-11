# Given an array of ints, return a new array length 2 containing the first and last elements
# from the original array. The original array will be length 1 or more.


def make_ends(input_list):
    result = [input_list[0], input_list[-1]]
    print(f"make_ends({input_list}) -> {result}")


make_ends([1, 2, 3])
make_ends([1, 2, 3, 4])
make_ends([7, 4, 6, 2])
