# Execute a string of code in python


def execute_string_code(string):
    print(string)
    print('-'*80)
    print(f'Result : {exec(string)}')


string_1 = """a = 6 + 5 
print(a)
"""

string_2 = """
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5))
"""

execute_string_code(string_1)
execute_string_code(string_2)