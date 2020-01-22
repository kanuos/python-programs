# Cloning or Copying a list

try:
    size = int(input('Enter the size of the list : '))
    user_list = []

    for index in range(size):
        while True:
            value = input(f'Enter the {index + 1} element : ')
            if value:
                user_list.append(value)
                break
            else:
                print('Value cannot be empty')

    print(f'Your entered list : {user_list}')
    clone_list = [x for x in user_list]

    while True:
        print(f'Original list : {user_list}')
        print(f'Clone list : {clone_list}')
        print('Press [1] to ADD, [2] to DELETE,[q] to QUIT')
        option = input('Enter your option here : ')
        if option == '1':
            while True:
                new_item = input('Enter new element to insert : ')
                if new_item:
                    clone_list.append(new_item)
                    break
                else:
                    print('Please insert valid element')
        elif option == '2':
            print(f'"{clone_list.pop()}" has been removed from list')
        elif option == 'q' or option =='Q':
            print('Exiting Program... Bye')
            break
        else:
            print('Invalid Option. Try Again')

except ValueError:
    print('Invalid Input')
