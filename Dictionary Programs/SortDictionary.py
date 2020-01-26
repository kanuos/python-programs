# Python | Sort Python dictionaries by Key or Value


def sort_dictionary(dictionary):
    my_dict = {}
    values_list = sorted(dictionary.values())
    for item in values_list:
        for k, v in dictionary.items():
            if v == item:
                my_dict[k] = v

    print(f'Dictionary sorted by Key : {dict(sorted(dictionary.items()))}')
    print(f'Dictionary sorted by Value : {my_dict}')


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
    sort_dictionary(user_dict)

except ValueError:
    print('Input cannot be empty.')
