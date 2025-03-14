#ex1
lis = [1, 12, 13, 14, 15, 2, 3]
result = [x for x in lis if x > 5 and x % 5 == 0]
print(result)  

#ex2
names = ["Ramzan", "Ali", "Ahmed"]
ages = [29, 30, 35]
result = {names[i]: ages[i] for i in range(len(names))}
print(result)  

#ex3
dict1 = {'key1': 4, 'key2': 5, 'key3': 3, 'key4': 9, 'key5': 8}
doubled_dict = {key: value * 2 for key, value in dict1.items()}
print(doubled_dict) 

#ex 4
string = "today is a sunny day"
count_u = string.lower().count('u')  
count_i = string.lower().count('i') 
total_count = count_u + count_i
print(total_count)  

#ex5
Lis = ["hello", "today", "is", "too", "cold"]
result = [item for item in Lis if len(item) > 3]
print(result)  
