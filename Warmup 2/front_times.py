# Given a string and a non-negative int n, we'll say that the front of the string
# is the first 3 chars, or whatever is there if the string is less than length 3.
# Return n copies of the front;


def front_times(string, n):
    return string[: min(3, len(string))] * n


user_arguments = [
    {"word": "Chocolate", "number": 2},
    {"word": "Chocolate", "number": 3},
    {"word": "Abc", "number": 3},
    {"word": "Ab", "number": 3}
]

for item in user_arguments:
    print(f"{item['word']} * {item['number']}  = {front_times(item['word'], item['number'])}")
