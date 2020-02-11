# Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
# The string length will be at least 2.


def extra_end(word):
    last_chars = word if len(word) < 2 else word[-2:]
    print(f"extra_end('{word}') -> {last_chars * 3}")


extra_end("Hello")
extra_end("ab")
extra_end("Hi")