# Given two strings, return True if either of the strings appears at the very end of the other
# string, ignoring upper/lower case differences (in other words, the computation should not be
# "case sensitive")


def end_other(first, second):
    first = first.lower()
    second = second.lower()
    result = False
    if first.endswith(second) or second.endswith(first):
        result = True
    print(f"end_other('{first}', '{second}') -> {result}")


end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc')
end_other('AbC', 'HiaBdc')
end_other('abc', 'abXabc')