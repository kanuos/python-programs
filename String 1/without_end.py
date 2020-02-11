# Given a string, return a version without the first and last char, so "Hello" yields "ell".
# The string length will be at least 2.


def without_end(word):
    print(f"without_end('{word}') -> '{word[1:-1]}'")


without_end("Hello")
without_end("java")
without_end("coding")
