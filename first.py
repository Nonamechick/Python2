import math
from functools import reduce
"""
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

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  

number1 = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, number1))
print(even_numbers)

product = reduce(lambda x,y: x*y,numbers)
print(product)

pairs = [(1,2),(4,1),(3,5)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)
"""

#ex 
"""

students = [
    {"name": "Alice", "score": 88, "age": 20},
    {"name": "Bob", "score": 92, "age": 22},
    {"name": "Charlie", "score": 88, "age": 19},
    {"name": "David", "score": 95, "age": 21}
]

sorted_students = sorted(students, key=lambda x: (-x["score"], x["age"]))
print(sorted_students)


words = ['apple', 'banana','cherry','blueberry','strawberry']

word = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(word)


num = [10,17,19,21,22,23,29,30,31]

prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

prime_numbers = list(filter(prime, num))

print(prime_numbers)

words1 = ['hi','hello','to','world', 'a','python']

modif = list(map(lambda word: word.upper() if len(word) > 3 else word, words1))

print(modif) 
"""


