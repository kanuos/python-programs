# Given 2 arrays of ints, a and b, return True if they have the same first element or
# they have the same last element. Both arrays will be length 1 or more.


def common_end(list1, list2):
    result = (list1[0] == list2[0]) or (list1[-1] == list2[-1])
    print(f"common_end({list1}, {list2}) -> {result}")


common_end([1, 2, 3], [7, 3])
common_end([1, 2, 3], [7, 3, 2])
common_end([1, 2, 3], [1, 3])