# How do you validate if an entered input is a valid email address?

import re

email = input('Enter email: ')

if re.match(r'[^@]+@[^@]+\.[^@]+', email):
    print('Valid email')
else:
    print('Invalid email')
