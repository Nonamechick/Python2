"""
squares = {x: x**2 for x in range(5)}
print(squares)

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)

parity = {x: "Even" if x % 2 == 0 else "Odd" for x in range(5)}
print(parity)

words = ['apple','banana','cherry']
word_length = {word: len(word) for word in words}
print(word_length)

nested_dict = {x: {y: y**2 for y in range(3)} for x in range(2) }
print(nested_dict) 

#ex
list = [1,2,3,5,6,4,3,6,7]
make = {s: s*s*s if s%2==1 else "Even" for s in list}
print(make)
"""
states = ['Andijan','Buxara','Samar']
capitals = ['Andijan','Buxara','Samarkand']
state_capital_dict = {states[i]: capitals[i] for i in range(len(states))}
print(state_capital_dict)

