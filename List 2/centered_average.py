# Return the "centered" average of an array of ints, which we'll say is the mean average of the
# values, except ignoring the largest and smallest values in the array. If there are multiple
# copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int
# division to produce the final average. You may assume that the array is length 3 or more.


def centered_average(array):
    smallest = min(array)
    largest = max(array)
    result_array = [x for x in array if x != largest and x != smallest]
    if array.count(smallest) > 1:
        result_array.append(smallest)
    if array.count(largest) > 1:
        result_array.append(largest)
    result = sum(result_array) // len(result_array)
    print(f"centered_average({array}) -> {result}")


centered_average([1, 2, 3, 4, 100])
centered_average([1, 1, 5, 5, 10, 8, 7])
centered_average([-10, -4, -2, -4, -2, 0])
