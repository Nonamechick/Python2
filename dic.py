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