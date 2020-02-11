# Given a string, return a string where for every char in the original, there are two chars.


def double_char(string):
    result = ""
    for char in string:
        result += char * 2
    print(f"double_char('{string}') -> '{result}'")


double_char('The')
double_char('AAbb')
double_char('Hi-There')
