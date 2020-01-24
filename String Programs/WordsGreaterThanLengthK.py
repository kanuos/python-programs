# Find words which are greater than given length k


def words_greater_than_k(string, k):
    word_list = string.split(' ')
    result = []
    for item in word_list:
        if len(item) >= k:
            result.append(item)
    return result


user_string = input('Enter the string : ')
if user_string:
    try:
        size_k = int(input('Enter the value of "k" : '))
        words_gt_k = words_greater_than_k(user_string, size_k)
        print(f'{user_string} has {len(words_gt_k)} words whose size is greater than or equal to {size_k}')
        print(words_gt_k)
    except ValueError:
        print('Value of K has to be a number')
else:
    print('String cannot be empty')