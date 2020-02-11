# Given an array of ints, return True if one of the first 4 elements in the array is a 9.
# The array length may be less than 4.


def array_front9(data):
    return 9 in data[:min( len(data), 4)]


first_list = [1, 2, 9, 3, 4]
second_list = [1, 2, 3, 4, 9]
third_list = [1, 2, 3, 4, 5]

print(f" Input : {first_list} ==> {array_front9(first_list)}")
print(f" Input : {second_list} ==> {array_front9(second_list)}")
print(f" Input : {third_list} ==> {array_front9(third_list)}")