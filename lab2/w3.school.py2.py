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