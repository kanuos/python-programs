# Given a string, return the count of the number of times that a substring length 2
# appears in the string and also as the last 2 chars of the string, so "hixxxhi"
# yields 1 (we won't count the end substring).


def last2(string):
    count = 0
    last_chars = string[-2:]
    # return string[:-2].count(last_chars)
    for i in range(len(string) - 3):
        if string[i] + string[i + 1] == last_chars:
            count += 1
    return count


input_strings = ["hixxhi", "xaxxaxaxx", "axxxaaxx"]
for item in input_strings:
    print(f'{item} -> {last2(item)}')
