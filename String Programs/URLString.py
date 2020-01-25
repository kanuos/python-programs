# Python | Check for URL in a String


def url_separator(string):
    words = string.split(' ')
    urls = []
    for item in words:
        if 'http' in item:
            urls.append(item)
    return urls


try:
    user_string = input('Enter the string: ')
    print(url_separator(user_string))
except ValueError:
    print('Invalid Input')