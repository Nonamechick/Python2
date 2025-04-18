import itertools
import operator
"""
result = itertools.count(start=0,step=2)
for number in result:
    if number<8:
        print(number)
    else:
        break
print(result)

res = itertools.cycle('123456')
counter =0
for number in result:
    if counter <10:
        print(number)
        counter = counter+1
    else:
        break
print(res)

r=itertools.repeat('hello',times=2)
for word in r:
    print(word) 
"""
list1 = [1, 2, 3]
tuple1 = ('a', 'b')
set1 = {10, 20}
combined_iterator = itertools.chain(list1, tuple1, set1)
print("Type of combined_iterator:", type(combined_iterator))

print("Elements in combined_iterator:")
for item in combined_iterator:
    print(item)

numbers = [1, 2, 3, 4, 5]

running_product = itertools.accumulate(numbers, operator.mul)

print("Running product:")
for value in running_product:
    print(value)

s = 10
st =1
print("start",s, "and",st)
my_co=itertools.count(s,st)
print("The never-end")
for i in my_co:
    print(i)
    break

def cycle_d(iter):
    return itertools.cycle(iter)
re = cycle_d(['A','B','C','D'])
print("The never-end")
for i in re:
    print(i)
    break

list_1 = ['a','b','c']
list_2 = ['d','e','f']
list_3 = ['1','2','3']
r1 = itertools.chain(list_1,list_2,list_3)
for element in r1:
    print(element)