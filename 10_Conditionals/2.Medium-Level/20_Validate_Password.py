# Validate Password

import re

password = input("Enter password: ")
if len(password) >= 8 and re.search(r"[A-Za-z]", password) and re.search(r"\d", password):
    print("Valid password")
else:
    print("Invalid password")

