# Handling missing keys in Python dictionaries


def del_missing_keys(dictionary):
    my_dict = {}
    for k, v in dictionary.items():
        if k:
            my_dict[k] = v
    return my_dict


def handle_missing_keys(dictionary, search_key):
    if search_key in dictionary.keys():
        return dictionary[search_key]
    else:
        return f'{search_key} not present in dictionary'


try:
    user_dict = {}
    size = int(input('Enter the size of the dictionary : '))
    for index in range(size):
        while True:
            key = input(f'Enter the {index + 1} key : ')
            value = input(f'Enter the {index + 1} value : ')
            print('-'*70)
            if key == 0 or key and value == 0 or value:
                user_dict[key] = value
                break
            else:
                print('Please enter valid Key and Value')
    refined_dict = del_missing_keys(user_dict)
    print(f'The refined dictionary : {refined_dict}')
    search_index = input('Enter the index you want to search : ')
    print(handle_missing_keys(user_dict, search_index))

except ValueError:
    print('Input cannot be empty.')
