# Given 2 strings, return their concatenation, except omit the first char of each.
# The strings will be at least length 1.


def non_start(first, second):
    print(f"non_start('{first}', '{second}') -> '{first[1:] + second[1:]}'")


non_start("Hello", "There")
non_start("java", "code")
non_start("shotl", "java")