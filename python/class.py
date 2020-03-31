# class is a constructor, or blueprint for creating objects 
# https://www.w3schools.com/python/python_classes.asp

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

## Methods are functions that belong to an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myFunction(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myFunction()

# modify object properties like this
p1.age = 40
print(p1.age)

# delete properties on objects 
#del p1.age

# Class Inheritance
###################################
# Create Parent Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

# create Child Class - by passing parent class
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

# if you want to keep parent's __init__ when creating child , do it like this : 
#class Student(Person):
#    def __init__(self, fname, lname):
#        Person.__init__(self, fname, lname)

# what if you want to add parameter
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)


# what if you want to add method to Student class

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
        
x = Student("Mike", "Olsen", 2019)
x.welcome()




































