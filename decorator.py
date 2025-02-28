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