# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".


def first_half(word):
    print(f'first_half("{word}") -> {word[:len(word)//2]}')


first_half("WooHoo")
first_half("HelloThere")
first_half("abcdef")
