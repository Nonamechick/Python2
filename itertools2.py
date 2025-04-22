import itertools as it
from itertools import islice, starmap, chain, combinations_with_replacement, groupby, accumulate, zip_longest

list_one = ['a','b','c']
# list_two = ['d','e','f']
# list_three = ['1','2','3']
# result = it.chain(list_one,list_two,list_three)
# for i in result:
#     print(i)

# names = ['Alice','James','Matt']
# have_flu = [True, True,False]
# res = it.compress(names, have_flu)
# for d in res:
#     print(d)

# my_list = [0,0,1,2,0]
# r = it.dropwhile(lambda x: x ==0, my_list)
# for o in r:
#     print(o)

# for k in islice(range(20),5):
#     print(k)
# li = [2,4,5,7,8,10,20]
# print(list(islice(li,1,6,2)))

# lo = [(2,5),(3,2),(4,3)]
# new_lo = list(starmap(pow,lo))
# print(new_lo)


my_list1 = [-4, -5, -1, 2, -7]
r1 = it.dropwhile(lambda x: x < 0, my_list1)
for o in r1:
    print(o)

r2 = it.combinations(my_list1, len(my_list1))
for j in r2:
    print(j)

r3 = it.permutations(my_list1, len(my_list1))
for s in r3:
    print(s)

r4 = it.count(10)
for a in r4:
    print(a)
    break


r5 = it.cycle(my_list1)
cycled_list = []
for i, val in enumerate(r5):
    if i == 15:
        break
    cycled_list.append(val)
print(cycled_list)



my_list1 = [-4, -5, -1, 2, -7]
my_list2 = [1, 2]  

def chain_lists():
    print(list(chain(my_list1)))

def combinations_with_repl():
    print(list(combinations_with_replacement(my_list1, len(my_list1))))

def group_consecutive():
    print([(key, len(list(group))) for key, group in groupby(my_list1)])

def accumulate_sum():
    print(list(accumulate(my_list1)))

def staggered_iterators(fill=None):
    print(list(zip_longest(my_list1, my_list2, fillvalue=fill)))
