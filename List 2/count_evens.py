# Return the number of even ints in the given array.


def count_evens(array):
    even_counter = 0
    for item in array:
        if item % 2 == 0:
            even_counter += 1
    print(f"count_evens({array}) -> {even_counter}")


count_evens([2, 1, 2, 3, 4])
count_evens([2, 2, 0])
count_evens([1, 3, 5])
