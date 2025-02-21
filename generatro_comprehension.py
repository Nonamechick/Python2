import math
"""
def count_up_to(limit):
    count = 0
    while count<limit:
        yield count
        count +=1
counter = (num for num in count_up_to(10))
for num in counter:
    print(num)

gen = (x for x in range(5))
print(next(gen))
print(next(gen))
"""

#ex
out = set()
gen = (x for x in range(21) if x % 2 == 0)  
out.update(gen)  
print(out)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

gen = (x for x in fibonacci(10))  
print(list(gen))  

numbers = [12, -5, 9, 0, -3, 7]
gen = (x for x in numbers if x <= 0) 
numbers = list(gen)  
print(numbers)

gen = (x**3 for x in range(1, 11)) 

print(list(gen))  


gen_primes = (x for x in range(2, 50) if all(x % d != 0 for d in range(2, int(x**0.5) + 1)))
print(list(gen_primes))

gen_filtered = (line for line in open("filename.txt") if "error" not in line)
print(list(gen_filtered))

sentence = "Python is fun and challenging"
gen_lengths = (len(word) for word in sentence.split())
print(list(gen_lengths))

gen_multiples = (3 * x for x in range(1, 6))
print(list(gen_multiples))

gen_divisible = (x for x in range(1, 51) if x % 3 == 0 and x % 5 == 0)
print(list(gen_divisible))

gen_factorial = (math.factorial(x) for x in range(1, 6))
print(list(gen_factorial))