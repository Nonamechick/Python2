#1
x = lambda a,b : a + b
print(x(2,3))
#2
u = [v for v in range(1,21) if v%2==0]
print(u)
#3
o = 'lambda'
vowels = 'aeiouAEIOU'
i = [d for d in o if d in vowels]
print(i)
#4
h = (s for s in range(1,11) if s%2==0 )
for num in h:
    print(num)
#5
def apply_function(func, numbers):
    return [func(x) for x in numbers]


def square(x):
    return x * x

def double(x):
    return x * 2

def add_one(x):
    return x + 1


numbers = [1, 2, 3, 4, 5]


squared = apply_function(square, numbers)
print(squared)  


doubled = apply_function(double, numbers)
print(doubled)  


incremented = apply_function(add_one, numbers)
print(incremented)  


cubed = apply_function(lambda x: x**3, numbers)
print(cubed)  


#6
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))
def fibonnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
print(fibonnaci(10))
#7
def add_hello_prefix(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (str, int, float)):
            raise TypeError("Function must return a string, int, or float")
        return "Hello, " + str(result)
    return wrapper


@add_hello_prefix
def get_name(name):
    return name

@add_hello_prefix
def get_list():
    return [1, 2, 3]  


try:
    print(get_name("Alice"))    
    print(get_list())          
except TypeError as e:
    print(f"Error: {e}")