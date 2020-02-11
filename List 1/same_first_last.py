# Given an array of ints, return True if the array is length 1 or more, and the first
# element and the last element are equal.


def same_first_last(input_list):
    print(f"same_first_last({input_list}) -> {input_list[0] == input_list[-1]}")


same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])