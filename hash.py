"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y 
        return False
    
point1 = Point(1,2)
point2 = Point(1,2)
point3 = Point(3,4)

points = {point1, point2, point3}
print(len(points))


def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False
print(is_hashable(42))
print(is_hashable([1,2,3]))"""

#ex 
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __hash__(self):
        return hash((self.brand, self.model, self.year))

    def __eq__(self, other):
        return (self.brand, self.model, self.year) == (other.brand, other.model, other.year)


car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Toyota", "Corolla", 2020)

car_set = {car1, car2, car3}
print(len(car_set))  

#ex2
mutable_list = [1, 2, 3]

try:
    dictionary = {mutable_list: "This will fail"}
except TypeError as e:
    print("Error:", e)  

#ex3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return self.x + self.y  

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


p1 = Point(1, 2)
p2 = Point(2, 1)  
p3 = Point(3, 0)

point_set = {p1, p2, p3}
print(len(point_set))  

#ex4
hashable_tuple = (1, 2, 3)
non_hashable_list = [1, 2, 3]

test_set = set()
test_set.add(hashable_tuple)

try:
    test_set.add(non_hashable_list)
except TypeError as e:
    print("Error:", e)  

#ex5
frozen_key = frozenset({1, 2, 3})

dictionary = {frozen_key: "This is a valid key"}
print(dictionary[frozen_key])  
