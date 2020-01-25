# String slicing in Python to rotate a string


def rotate_string(string, index):
    left_rotate = string[index:]
    remaining_chars = string[:index]
    left_rotate += remaining_chars

    right_rotate = string[:-index]
    remaining_chars = string[-index:]
    right_rotate = remaining_chars + right_rotate
    return {
        'left': left_rotate,
        'right': right_rotate
    }


try:
    user_string = input('Enter the string : ')
    rotation = int(input('Enter the rotation index : '))
    if rotation > len(user_string):
        print('Index cannot be bigger than string length')
    else:
        result = rotate_string(user_string, rotation)
        print(f'Left rotation : {result["left"]}')
        print(f'Right rotation : {result["right"]}')

except ValueError:
    print('Invalid Input')