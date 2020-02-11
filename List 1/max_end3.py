# Given an array of ints length 3, figure out which is larger, the first or last element
# in the array, and set all the other elements to be that value. Return the changed array.


def max_end3(input_list):
    filler = max(input_list[0], input_list[-1])
    result = [filler, filler, filler]
    print(f"max_end3({input_list}) -> {result}")


max_end3([1, 2, 3])
max_end3([11, 5, 9])
max_end3([2, 11, 3])
