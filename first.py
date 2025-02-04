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