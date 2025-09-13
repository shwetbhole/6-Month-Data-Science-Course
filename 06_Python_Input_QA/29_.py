# How would you check if a string contains only alphabets using `input()`?

user_input = input('Enter a string: ')

if user_input.isalpha():
    print('Only alphabets')
else:
    print('contains non-alphabets characters')
