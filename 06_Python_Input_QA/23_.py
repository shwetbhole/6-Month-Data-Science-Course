# Write a program that asks the user for a year and determines if it's a leap year.

year = int(input('Enter a number: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Leap year')
else:
    print('Not a leap year')