def log_call(func):
    def wrapper(*args):
        print("Function:", func.__name__)
        print("Arguments:", args)
        return func(*args)
    return wrapper
@log_call
def add(a, b):
    return a + b
@log_call
def greet(name):
    return f"Hello {name}"
@log_call
def square(n):
    return n * n
print(add(2, 3))
print(greet("dhanashyam"))
print(square(5))