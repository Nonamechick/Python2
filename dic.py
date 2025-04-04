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