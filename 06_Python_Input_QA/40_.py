# Write a program to check if the entered string has digits.

user_input = input('Enter a number: ')

if any(char.isdigit() for char in user_input):
    print('Contain digits')
else:
    print('No digits')