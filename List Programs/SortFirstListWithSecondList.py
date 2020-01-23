# Python | Sort the values of first list using second list

# get two lists

# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]

list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

if len(list1) < len(list2):
    print('Two lists are not of same size. Cannot be sorted')
else:
    size = len(list2)
    merged_list = []
    sorted_array = []
    for index in range(size):
        temp_tuple = (list2[index], list1[index])
        merged_list.append(temp_tuple)
    print(f'List 1 : {list1}')
    print(f'List 2 : {list2}')
    print(' list 1 when sorted by list 2 returns : ')
    merged_list.sort()
    for k,v in merged_list:
        sorted_array.append(v)
    print(sorted_array)


