# Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M

#get input
try:
    num = int(input('Enter the length of the array : '))
    user_array = []
    for i in range(num):
        while True:
            value = int(input(f'Enter the {i + 1} element : '))
            if value >= 0:
                user_array.append(value)
                break
            else:
                print('Please enter valid element')

    m_value = int(input('Enter the value of M : '))
    if not m_value:
        print('Enter valid value for M ')
    else:
        print(f'The original list : {user_array}')
        for i in range(1,num):
            user_array[i] = (user_array[i-1] + 1) % m_value
        print(f'The reconstructed list : {user_array}')
except ValueError:
    print('Invalid Input')