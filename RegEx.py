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

