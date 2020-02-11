#  Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array


def array123(array):
    return 1 in array and 2 in array and 3 in array


input_user = [
    [1, 1, 2, 3, 1], [1, 1, 2, 4, 1], [1, 1, 2, 1, 2, 3]
]

for item in input_user:
    print(f"{item} -> {array123(item)}")
