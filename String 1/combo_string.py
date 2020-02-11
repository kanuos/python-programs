# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter
# string on the outside and the longer string on the inside.
# The strings will not be the same length, but they may be empty (length 0).


def combo_string(first, second):
    smaller = first if len(first) < len(second) else second
    bigger = first if len(first) > len(second) else second
    print(f"combo_string('{first}', '{second}') -> {smaller + bigger + smaller} ")


combo_string("Hello", "hi")
combo_string("hi", "Hello")
combo_string("aaa", "b")
