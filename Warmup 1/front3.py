# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.


def front3(string):
    if len(string) < 3:
        return string * 3
    return string[:3] * 3


print(front3("java"))
print(front3("chocolate"))
print(front3("abc"))
print(front3("ok"))
