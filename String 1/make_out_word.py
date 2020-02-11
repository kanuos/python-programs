# Given an "out" string length 4, such as "<<>>", and a word, return a new string where
# the word is in the middle of the out string, e.g. "<<word>>".


def make_out_word(tags, text):
    start_tags = tags[:2]
    end_tags = tags[2:]
    print(f"make_out_word('{tags}', '{text}') -> '{start_tags + text + end_tags}'")


make_out_word('<<>>', "Yay")
make_out_word('<<>>', "WooHoo")
make_out_word('[[]]', "word")
