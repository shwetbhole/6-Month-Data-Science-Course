# How would you accept and store multiple names from the user?

import re

text = input('Enter a string: ')

numbers = re.findall(r'\d+', text)
print('Extracted numbers:', numbers)