import math


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

def cubeVolume(n):
    return n**3
print(cubeVolume(4))
print(cubeVolume(cubeVolume(3)))

def anotherCube(n):
    return ((math.sqrt(3) * n*n*n) / 9)
print(anotherCube(4))

def squareArea(n):
    return n*n

print(squareArea(5))

def mystery(x,y):
    res = (x+y)/(y-x)
    return res
print(mystery(2,3))