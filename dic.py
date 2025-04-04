from functools import reduce
"""

car_dict = {'a': 'Mercedes-Benz','b': 'BWM', 'c': 'Ferrari', 'd': 'Lamborghini','e':'Jeep'}

car_dict = dict(map(lambda x: (x[0], x[1]+'_'), car_dict.items() ))
print('The modified dictionary is : ')
print(car_dict)

def example(i):
    return i%3
set_exm = {33,102,62,96,44,28,227}
upd_itm = map(example,set_exm)
print(upd_itm)
print(set(upd_itm))

def myMapFunc(list1,list2):
    return list1+list2
my_list1 = [2,3,4,5,6,7,8,9]
my_list2 = [4,8,12,18,20,24,28]
updated_list= map(myMapFunc, my_list1,my_list2)
print(updated_list)
print(list(updated_list))

num = [12,37,34,26,9, 250, 451,3,10]
even = list(filter(lambda x: (x%2==0), num))
print(even)

product = reduce((lambda x, y: x*y), [1,2,3,4])
print(product)

"""
# def double(i):
#     return i*2
# num = [1,2,3,4]
# upd = map(double, num)
# print(list(upd))

# n = ['1','2','3']
# con = map(int, n)
# print(list(con))

# print(list(map((lambda x:x**2), [1,2,3,4])))

# d = [1,2,3]
# s = [4,5,6]
# o = map(lambda x, y: x+y,d,s)
# print(list(o))

# def convert(i):
#     return (i*(9/5)) +32
# p = list(map(convert, [0,25,100]))
# print(p)

num = [11,6,33,21,9, 2, 451,3,4]
even = list(filter(lambda x: (x%2==0), num))
print(even)

print(list(map(len, ['kottt','dsdsds','dsdsds'])))

print(list(map(str.upper, ['apple', 'banana', 'cherry'])))

print(list(map(lambda x: (x**2) * 2, [1, 2, 3, 4])))

d = (1,2,5)
s = (2,5,6)
o = map(lambda x, y: x+y,d,s)
print(list(o))