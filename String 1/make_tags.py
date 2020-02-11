# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text.
# In this example, the "i" tag makes <i> and </i> which surround the word "Yay".
# Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".


def make_tags(tag, text):
    tag = tag.lower()
    print(f"make_tags('{tag}', '{text}') -> <{tag}>{text}</{tag}>")


make_tags('i', 'Yay')
make_tags('i', 'Hello')
make_tags('cite', 'Yay')
