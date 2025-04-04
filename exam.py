import math

def mul(i):
    return i*i
x = map(mul, (3,5,7,11,13))
print(x)
print(list(x))

exa = ['welcome','to','simplelearn']
x = list(map(len, exa))
print(x)

num = [9,36,49,81,121]
x =list(map(math.sqrt, num))
print(x)

n = (6,9,21,44)
res = map(lambda i: i+i, num)
print(list(res))

def upper(d):
    return d.upper()
stri = 'This is Pythonlesson'
upd_list = map(upper, stri)
print(upd_list)
print(list(upd_list))


l = ['sat', 'bat','cat','mat']
test = list(map(list,l))
print(test)


def example(s):
    return s.upper()
tuple_exm = ('this','is','map','in','python','article')
upd_tup = map(example, tuple_exm)
print(upd_tup)
print(tuple(upd_tup))