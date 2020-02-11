# Given a string, return a new string made of every other char starting with the first,
# so "Hello" yields "Hlo".


def string_bits(word):
    return word[::2]


word_list = ["Hello", "Hi", "Heeololeo", "Sounak"]

for word in word_list:
    print(f"{word} -> '{string_bits(word)}'")
