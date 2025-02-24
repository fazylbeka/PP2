import re
txt = 'The rain in Spain'
x = re.findall('[a-c]', txt)
print(x)
#result: ['a', 'a']

import re
txt = 'The rain in Spain'
x = re.search('a', txt)
print(x.start())
#result: 5

import re
txt = 'The rain in Spain'
x = re.search('\s', txt)
print(x.start())
#result: 3

#lab5

#1
import re

txt = "The rain in Spain"
x = re.search("rain", txt)  # Searches for 'rain' in the string

if x:
    print("Match found!")
else:
    print("No match")
#result: Match found!

#2
import re

pattern = re.compile(r"\d+")  # Compile regex to match digits
txt = "There are 123 apples and 456 bananas"

matches = pattern.findall(txt)  # Find all matches
print(matches)
#result: ['123', '456']



