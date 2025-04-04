car_dict = {'a': 'Mercedes-Benz','b': 'BWM', 'c': 'Ferrari', 'd': 'Lamborghini','e':'Jeep'}

car_dict = dict(map(lambda x: (x[0], x[1]+'_'), car_dict.items() ))
print('The modified dictionary is : ')
print(car_dict)