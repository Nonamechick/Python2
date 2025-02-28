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