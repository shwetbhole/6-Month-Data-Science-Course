# Validate  an email format

import re   # importing the regular expression

email = input("Enter email: ")

if re.match(r"^[\w\.-]+@[\w\.-]+\.(com|org|net|edu)$", email):
    print("Email is valid")
else:
    print("Email is not valid")
