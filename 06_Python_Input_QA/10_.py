# How would you check if a string is a palindrome using `input()`?

text = input('Enter a string: ')

if text == text[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')