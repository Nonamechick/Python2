# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# student1 = Student("Jo", 70)
# print(student1.name)
# print(student1.age)

# class Faculty:
#     def putdata(self):
#         self.id=int(input('enter id'))
#         self.name=input('enter name')
#         self.salary = float(input('enter faculty salary'))
#     def display(self):
#         print('faculty id: ', self.id)
#         print('faculty name:', self.name)
#         print('faculty salary: ', self.salary)
# a=Faculty()
# a.putdata()
# a.display()
"""
class Faculty1:
    def __init__(self,a,b,c):
        self.f_id=a
        self.name =b
        self.salary = c
    def display(self):
        print('faculty id: ', self.f_id)
        print('faculty name: ', self.name)
        print('faculty salary: ', self.salary)
a=Faculty1(1,'Varun', 10000)
a.display()

class Student:
    def __init__(self, name='Unknown', age=18):
        self.name = name
        self.age= age
student1 = Student('Alice',22)
student2 = Student()

print(student1.name, student1.age)
print(student2.name, student2.age)"
"""

class Person:
    def __init__(self,firstName, lastName, name='Unknown'):
        self._name = lastName+", " +firstName
        self.name = name
harry = Person("Harry", "Morgan")
print(harry._name)
p = Person('unknown','unknown')
print(p.name)

class Service:
    def __init__(self, str_description, value_price):
        self.str_description = str_description
        self.value_price = value_price
    def display(self):
        print('enter description', self.str_description)
        print('enter value price', self.value_price) 
service1 = Service('jfsajfak',4241)
service1.display()
class Item:
    def __init__(self,smth, fl):
        self.smth = smth
        self.fl = fl
    def display(self):
        print('enter', self.smth)
        print('enter', self.fl)
st=Item('cete',424)
st.display()