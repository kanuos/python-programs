# Ways to sort list of dictionaries by values in Python – Using itemgetter
from operator import itemgetter


def sort_by_value(list_dictionary, value):
    return sorted(list_dictionary, key=lambda i: i[value])


user_dicts = [
    {
        "name": "Kappa",
        "age": 31,
        "rank": 8
    },
    {
        "name": "Pi",
        "age": 29,
        "rank": 15
    },
    {
        "name": "Theta",
        "age": 27,
        "rank": 18
    },
    {
        "name": "Upsilon",
        "age": 18,
        "rank": 4
    },
    {
        "name": "Alpha",
        "age": 55,
        "rank": 2
    },
    {
        "name": "Beta",
        "age": 52,
        "rank": 3
    },
    {
        "name": "Delta",
        "age": 50,
        "rank": 6
    },
    {
        "name": "Gamma",
        "age": 48,
        "rank": 1
    }
]

print('Input List of Dictionary : ')
print(user_dicts)

all_keys = []

for dicts in user_dicts:
    for k, v in dicts.items():
        if k not in all_keys:
            all_keys.append(k)

for item in all_keys:
    print(f'Sorted by {item} : ')
    print(sort_by_value(user_dicts, item))
