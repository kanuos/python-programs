# Python | Merging two Dictionaries


def merge_dict_1(dictionary1, dictionary2):
    for k, v in dictionary2.items():
        dictionary1[k] = v
    return dictionary1

def merge_dict_2(dictionary1, dictionary2):
    return {
        **dictionary1, **dictionary2
    }


sounak = {
    'name': 'Sounak',
    'age': 31,
    'gender': 'M'
}

plan = {
    'technology': ['web development',
                   'android development',
                   'hybrid development',
                   'machine learning and data science'],
    'website': 'www.sounak.io'
}

print('The merged dictionary : ')
print('Method 1')
print(merge_dict_1(sounak, plan))
print('Method 2')
print(merge_dict_2(sounak, plan))
