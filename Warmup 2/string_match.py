# Given 2 strings, a and b, return the number of the positions where they contain the
# same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az"
# substrings appear in the same place in both strings.


def sub_string_of_length_2(string):
    sub_strings = []
    for index in range(len(string) - 1):
        sub_strings.append(string[index] + string[index + 1])
    return sub_strings


def generate_result(first, second):
    first_list = sub_string_of_length_2(first)
    second_list = sub_string_of_length_2(second)
    common = [x for x in first_list if x in second_list]
    print(f"string_match('{first}', '{second}') -> {len(common)} common sub-strings")
    print(f" The commmon sub strings are : {common}")
    print("=" * 90)


generate_result("xxcaazz", "xxbaaz")
generate_result("abc", "abc")
generate_result("abc", "axc")
