# Counting the frequencies in a list using dictionary in Python


def measure_frequency(operation_list):
    frequency_dict = {}
    for entry in operation_list:
        if entry not in frequency_dict.keys():
            frequency_dict[entry] = operation_list.count(entry)
    return frequency_dict


try:
    size = int(input('Enter the size of the list : '))
    user_list = []
    for index in range(size):
        while True:
            value = input(f'Enter the {index+1} value : ')
            if value == 0 or value:
                user_list.append(value)
                break
            else:
                print('Invalid input. Try again')
    frequency = measure_frequency(user_list)
    print(f'The frequency of items of {user_list} :')
    for k, v in frequency.items():
        print(f'Item "{k}" present {v} times')
except ValueError:
    print('Invalid Input. Exit')
