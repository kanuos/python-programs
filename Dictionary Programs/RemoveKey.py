# Python | Ways to remove a key from dictionary


def remove_key_1(dictionary, del_key):
    my_dict = {}
    if del_key not in dictionary.keys():
        return {
            'result': f'No key of {del_key} present in {dictionary}',
            'removed': None
        }
    for k, v in dictionary.items():
        if k != del_key:
            my_dict[k] = v
    return {
        'result': f'Resultant Dictionary : {my_dict}',
        'removed': f'("{del_key}": "{dictionary[del_key]}")'
    }


def remove_key_2(dictionary, del_key):
    removed = dictionary[del_key]
    my_dict = {x: y for x, y in dictionary.items() if x != del_key}
    return {
        'result': my_dict,
        'removed': f'"{del_key}" : "{removed}"'
    }


def remove_key_3(dictionary, del_key):
    removed = dictionary[del_key]
    del dictionary[del_key]
    return {
        'result': dictionary,
        'removed': f'"{del_key}" : "{removed}"'
    }


def remove_key_4(dictionary, del_key):
    removed = dictionary[del_key]
    del dictionary[del_key]
    return {
        'result': dictionary,
        'removed': f'"{del_key}" : "{removed}"'
    }


def remove_key_5(dictionary, del_key):
    removed = dictionary.pop(del_key)
    return {
        'result': dictionary,
        'removed': f'"{del_key}" : "{removed}"'
    }


try:
    size = int(input('Enter the size of the dictionary : '))
    user_dict = {}
    for index in range(size):
        while True:
            key = input(f'Enter the {index + 1} key : ')
            value = input(f'Enter the {index + 1} value : ')
            print('_'*80)

            if (key or key == 0) and (value or value == 0):
                user_dict[key] = value
                break
            else:
                print(f'Invalid key or value for {index + 1} element')

    key_to_remove = input('Enter the KEY to remove : ')

    # result = remove_key_1(user_dict, key_to_remove)
    # print('DELETE USING METHOD:1')
    # print(result["result"])
    # print(f'Item removed :{result["removed"]}')
    # print('='*80)
    #
    result = remove_key_2(user_dict, key_to_remove)
    print('DELETE USING METHOD:2')
    print(result["result"])
    print(f'Item removed :{result["removed"]}')
    print('=' * 80)
    #
    # result = remove_key_3(user_dict, key_to_remove)
    # print('DELETE USING METHOD:3')
    # print(result["result"])
    # print(f'Item removed :{result["removed"]}')
    # print('='*80)
    #
    # result = remove_key_4(user_dict, key_to_remove)
    # print('DELETE USING METHOD:4')
    # print(result["result"])
    # print(f'Item removed :{result["removed"]}')
    # print('='*80)
    #
    # result = remove_key_5(user_dict, key_to_remove)
    # print('DELETE USING METHOD:5')
    # print(result["result"])
    # print(f'Item removed :{result["removed"]}')
    # print('='*80)

except ValueError:
    print('Invalid Input')
