def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print('After function call')
    return wrapper
@my_decorator
def hello():
    print('Hell, World')
hello()

def decorator_function(original_function):
    def wrapper_function():
        print('Wrapper executed this before {}'. format(original_function.__name__))
        return original_function()
    return wrapper_function
@decorator_function
def display():
    print('Display function executed')
display()

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} was called with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper
@log_function_call
def add(a,b):
    return a+b
@log_function_call
def multiple(a,b):
    return a*b

print(add(5,10))
print(multiple(2,3))

def print_output(should_print):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if should_print:
                print(f"Function output: {result}")
            return result
        return wrapper
    return decorator
@print_output(should_print=True)
def add(a,b):
    return a+b
print(add(5,3))