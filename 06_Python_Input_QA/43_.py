# Write a program to find the sum of all digits in a string entered by the user.
from unicodedata import digit

user_input = input('Enter a string: ')

digit_sum = sum(int(digit) for digit in user_input if digit.isdigit())

print('Sum of digits: ', digit_sum)