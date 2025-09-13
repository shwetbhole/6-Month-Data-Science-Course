# How do you check if a string entered by the user contains any punctuation?

import string
text = input('Enter a string: ')

if any(char in string.punctuation for char in text):
    print('Contains punctuation')
else:
    print('No punctuation')