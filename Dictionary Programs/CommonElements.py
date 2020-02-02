# Python | Find common elements in three sorted arrays by dictionary intersection


def common_elements(first_list, second_list, third_list):
    return [x for x in first_list if x in second_list and x in third_list]


def common_elements_using_set(first_list, second_list, third_list):
    third_set = set(third_list)
    final_set = set(first_list).intersection(set(second_list))
    return list(final_set.intersection(third_set))


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(common_elements(ar1, ar2, ar3))
print(common_elements_using_set(ar1, ar2, ar3))


ar1 = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]


print(common_elements(ar1, ar2, ar3))
print(common_elements_using_set(ar1, ar2, ar3))
