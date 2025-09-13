# How do you prevent a user from entering an empty string?

user_input = input('Enter something: ').strip()

if not user_input:
    print('Input cannot be empty.')
else:
    print('You entered: ', user_input)