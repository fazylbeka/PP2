#Python Booleans
print(10 > 9)
#True

print(10 == 9)
#False

print(10 < 9)
#False

print(bool("abc"))
#True

print(bool(0))
#False

#Python Operators
print(10 * 5)

print(10 /2)

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

if 5 !=10:
  print("5 and 10 is not equal")

if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#Python Lists
#1Python Lists

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))

#Python - Access List Items
mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])
# answer: cherry

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Python - Change List Items
fruits = ["apple", "banana", "cherry"]
fruits[0]= "kiwi"

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])
#Answer: mango

#Python - Add List Items
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)

#Python - Remove List Items
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

fruits = ['apple', 'banana', 'cherry']
fruits.clear()

#Python - Loop Lists
mylist = ['apple', 'banana', 'cherry']
i = 0
while i < len(mylist):
  print(mylist[i])
  i = i + 1

#Python - List Comprehension
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

#Python - Sort Lists
#What is a correct syntax for sorting a list?
mylist.sort()

#What is a correct syntax for reversing the current order of a list?
mylist.reverse()

#What is a correct syntax for sorting a list descending?
mylist.sort(reverse = True)

#What is a correct syntax for making a copy of a list?
list2 = list()

#What is a correct syntax for making a copy of a list?
#list2 = list(list1)

#What is a correct syntax 1.copyfor making a copy of a list?
#list2 = list1[:]

#Python - Join Lists
#What is a correct syntax for joining list1 and list2 into list3?
#list3 = list1 + list2

#What is a correct syntax for adding elements from list2 into list1?
#list1.extend(list2)

#Python Tuples
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Python - Access Tuple Items
fruits = ("apple", "banana", "cherry")
print(fruits[0])

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Python - Unpack Tuples
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#y= banana, cherry

#Python - Loop Tuples
mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#Python Sets
fruits = {'apple', 'banana', 'cherry'}
print(len(fruits))

#Python - Access Set Items
fruits = {"apple", "banana", "cherry"}
if "apple" infruits:
  print("Yes, apple is a fruit!")

#Python - Add Set Items
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Python - Remove Set Items
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Python - Loop Sets

myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)

#Python Dictionaries
x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

#Python - Access Dictionary Items
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Python - Change Dictionary Items
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964

}
car["year"] = 2020

#Python - Add Dictionary Items
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

x = {'type' : 'fruit', 'name' : 'apple'}
x.update({'color' :'green'})

#Python - Remove Dictionary Items

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#Python - Loop Dictionaries

myset = {'apple', 'banana', 'cherry'}
for x  in myset:
  print(x)

#Python - Nested Dictionaries
a = {'name': 'John', 'age': 20}
b = {'name': 'May', 'age': 23}
customers = {'c1': a, 'c2': b}
for x, obj in customers.items():
  print(x)
for y in obj:
  print(y + ':', obj[y])

#Python If ... Else
a = 50
b = 10
if a >b:
  print("Hello World")

a = 50
b = 10
if a !=b:
  print("Hello World")

a = 50
b = 10
if a ==b:
  print("Yes")
else:
  print("No")

a = 50
b = 10
if a ==b:
  print("1")
elif a >b:
  print("2")
else:
  print("3")

if 5 > 2:
    print("YES")

#Python While Loops
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x)