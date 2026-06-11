def log_call(func):
    def wrapper(*args):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}")
        result = func(*args)
        return result
    return wrapper
@log_call
def greet(name):
    print(f"Hello, {name}!")
@log_call
def add(a, b):
    print(f"Sum = {a + b}")
@log_call
def multiply(a, b):
    print(f"Product = {a * b}")
greet("dhanashyam")
add(5, 10)
multiply(5,5)