# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


def hello_name(word):
    return f"Hey, {word}!" if len(word) > 0 else "Hey, Stranger"


def print_result(string):
    print(f'hello_name("{string}") -> "{hello_name(string)}"')


print_result("Bob")
print_result("Alice")
print_result("X")
print_result("")