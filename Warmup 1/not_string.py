# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.


def not_string(string):
    if string.startswith("not"):
        return string
    return "not " + string


print(not_string("candy"))
print(not_string("x"))
print(not_string("not bad"))
