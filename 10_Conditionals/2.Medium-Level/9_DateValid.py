# Determine if a given date is valid

import calendar

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if 1 <= month <= 12 and 1 <= day <= calendar.monthrange(year, month)[1]:
    print("Valid date")
else:
    print("Invalid date")