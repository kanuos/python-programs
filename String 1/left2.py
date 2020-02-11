# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
# The string length will be at least 2.


def left2(word):
    print(f"left2('{word}') -> '{word[2:] + word[:2]}'")


left2("Hello")
left2("java")
left2("Hi")