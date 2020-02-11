# Return the number of times that the string "code" appears anywhere in the given string, except
# we'll accept any letter for the 'd', so "cope" and "cooe" count.
import re


def count_code(string):
    # using regex to find anything that has co*e  where * can be anything from a-z
    print(f"count_code('{string}') -> {len(re.findall('co[a-z]e', string))}")


count_code('aaacodebbb')
count_code('codexxcode')
count_code('cozexxcope')
