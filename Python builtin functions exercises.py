#Python builtin functions exercises
#1. Write a Python program with builtin function to multiply all the numbers in a list
from functools import reduce
from operator import mul

def multiply_list(numbers):
    return reduce(mul, numbers)

numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print(result)

#2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())

    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

input_string = input("Enter a string: ")
count_case(input_string)

#3. Write a Python program with builtin function that checks whether a passed string is palindrome or not
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#4. Write a Python program that invoke square root function after specific milliseconds
import time
import math
def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay_ms} milliseconds is {result}")
num = int(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))

delayed_sqrt(num, delay)

#5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(tup):
    return all(tup)

sample_tuple = (True, 1, "Hello", 5)
print(all_true(sample_tuple))

sample_tuple2 = (True, 0, "Hello")
print(all_true(sample_tuple2))





