# Python | Convert a list of Tuples into Dictionary


def convert_to_dictionary(tuple_list):
    tuple_list_dict = {}
    for item in tuple_list:
        tuple_list_dict[item[0]] = [(item[1])]
    del tuple_list
    return tuple_list_dict


try:
    user_list = []
    size = int(input('Enter the size of the list : '))
    for index in range(size):
        while True:
            print('To enter a tuple use spaces between values.')
            value = input(f'Enter the {index+1} tuple : ')
            if value == 0 or value:
                first, second = value.split(' ')
                user_list.append((first, int(second)))
                break
            else:
                print('Error! Try again')
    print(f'The converted dictionary : \n {convert_to_dictionary(user_list)}')
    print(f'Type of Input : {type(user_list)}')
    print(f'Type of Output : {type(convert_to_dictionary(user_list))}')
except ValueError:
    print('Invalid Input. Program exiting gracefully.')
