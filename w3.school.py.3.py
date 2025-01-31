#Python Functions
def my_function():
    print("Hello from a function")

my_function()

def my_function(fname, lname):
  print(fname)


def my_function(x):
    return x + 5

def my_function(*kids):
  print("The youngest child is " + kids[2])

def my_function(**kid):
  print("His last name is " + kid["lname"])

#Python Lambda
x =lambda a: a

#Python Arrays
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])

fruits = ['apple', 'bananan', 'cherry']
print(len(fruits))

#Python Classes and Objects
class MyClass: x = 5

class MyClass:
  x = 5
p1 = MyClass()

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
    self.name = name
    self.age = age

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

#Python Inheritance
class Student(Person):
    class Person:
        def __init__(self, fname):
            self.firstname = fname

        def printname(self):
            print(self.firstname)

    class Student(Person):
        pass

    x = Student("Mike")
    x.printname()

