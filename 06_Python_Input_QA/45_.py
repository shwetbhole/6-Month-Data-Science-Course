# How would you check if a string entered by the user contains any uppercase letters?

user_input = input('Enter a string: ')

if any(char.isupper() for char in user_input):
    print('Contains uppercase letters')
else:
    print('No uppercase letters')