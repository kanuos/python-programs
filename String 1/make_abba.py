# Given two strings, a and b, return the result of putting them together in the order abba,
# e.g. "Hi" and "Bye" returns "HiByeByeHi".


def make_abba(first, second):
    print(f"make_abba('{first}', '{second}') -> '{first + second * 2 + first}'")


make_abba("Hi", "Bye")
make_abba("Yo", "Alice")
make_abba("What", "Up")
