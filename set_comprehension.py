"""
numbers = [1,2,3,4,5,6,6,3,5,6]
unique_squares = {x**2 for x in numbers}
print(unique_squares)

words = ['apple','banana','apple','cherry','banana']
unique_words = {word for word in words}
print(unique_words)

even_numbers = {x for x in range(10) if x%2==0}
print(even_numbers)

sentence = "Python programming is hell easy"
vowels = {char for char in sentence if char in 'aeiouAEIOU'}
print(vowels)

list = [1,2,3,5,6,4,3,6,7]
out =set()
make = {s: out.add(s) if s%2==0 else "Odd" for s in list}
print(make)
print(out)
"""
#ex1
def is_proper_subset(s, t):
    return s < t  
S = {1, 2}
T = {1, 2, 3, 4}

print(is_proper_subset(S, T))  

S2 = {1, 2, 3, 4}
print(is_proper_subset(S2, T))

#ex2
def common_strings(s, t):
    return s & t  


S = {"apple", "banana", "cherry"}
T = {"banana", "cherry", "date", "fig"}

print(common_strings(S, T))  
#ex3
def unique_strings(s, t):
    return s - t  

S = {"apple", "banana", "cherry"}
T = {"banana", "cherry", "date", "fig"}

print(unique_strings(S, T))  
#ex4
s =set()
for i in range(1,5):
    s.add(i*i)
    s.add(-i)
print(s)
#ex5
for i in range(0,20,2):
    s.add(i)
for i in range(0,20,3):
    s.discard(i)
print(s)
