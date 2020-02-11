# Return the sum of the numbers in the array, except ignore sections of numbers starting with a
# 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


def sum67(array):
    copy = [x for x in array]
    omit, index_6, index_7 = [], [], []
    for i in range(len(array)):
        if array[i] == 6:
            index_6.append(i)
        elif array[i] == 7:
            index_7.append(i)
    for i in range(len(index_6)):
        if index_6[i] < index_7[i]:
            omit.append((index_6[i], index_7[i]))
    if len(omit) == 0:
        result = sum(array)
    else:
        omit.reverse()
        temp = []
        for (start, end) in omit:
            temp.extend(array[:start])
            temp.extend(array[end+1:])
            array = [x for x in temp]
            temp = []
        result = sum(array)
    print(f"sum67({copy}) -> {result}")


sum67([1, 2, 2])
sum67([1, 2, 2, 6, 99, 99, 7])
sum67([1, 1, 6, 7, 2])
sum67([1, 1, 6, 7, 2,6,99, 99, 5, 7, 3])
sum67([1, 1, 6, 7, 2])
