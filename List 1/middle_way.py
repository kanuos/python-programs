# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their
# middle elements.


def middle_way(list1, list2):
    result = [list1[1], list2[1]]
    print(f"middle_way({list1}, {list2}) -> {result}")


middle_way([1, 2, 3], [4, 5, 6])
middle_way([7, 7, 7], [3, 8, 0])
middle_way([5, 2, 9], [1, 4, 5])