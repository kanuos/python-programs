# Given an array of ints, return the number of 9's in the array.


def array_count9(arr):
    return arr.count(9)


user_arrays = [[1, 2, 9], [1, 9, 9], [1, 9, 9, 3, 9]]

for array  in user_arrays:
    print(f"array_count9({array}) -> {array_count9(array)}")

