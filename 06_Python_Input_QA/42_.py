# Write a program to check if the entered string has only whitespace characters.

user_input = input('Enter a string: ')

if user_input.isspace():
    print('Contains whitespace.')
else:
    print('Contains non-whitespace characters')

# isspace() checks if every character in the string is whitespace (space, tab, newline).
# It returns:
# True → if the string is made of only spaces (or whitespace).
# False → if there’s at least one non-space character.
