# Count the Number of matching characters in a pair of string


def count_number_matching(string1, string2):
    matching_chars = []
    for char in string1:
        for match in string2:
            if match == char:
                if match not in matching_chars:
                    matching_chars.append(match)
    return {
        'output': len(matching_chars),
        'matching': matching_chars
    }


user_string = input('Enter the first string : ')
user_string_2 = input('Enter the second string : ')
result = count_number_matching(user_string, user_string_2)

print(f'The count of matching characters : {result["output"]}')
print(f'The matching characters are : {result["matching"]}')
