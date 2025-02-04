def greet():
    print("No hello")
greet()

def add(a,b):
    return a+b
print(add(5,3))

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(3,3))

def calculate(a,b):
    sum_res = a+b
    product = a*b
    return sum_res, product
s,p = calculate(4,5)
print("sum",s)
print("product",p)

def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume
res1 = cubeVolume(2)
res2 = cubeVolume(10)
print("res1",res1)
print("res2",res2)

def recrangleArea(w, l):
    return w*l
print(recrangleArea(4,5))


def is_even(check):
    if check % 2 == 0:
        return "It's even"

print(is_even(10))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(6))  
