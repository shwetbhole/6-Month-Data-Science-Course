# Write a program to check if an entered number is a perfect square.

import math

num = int(input('Enter a number: '))

if math.isqrt(num)**2 == num:
    print('Perfect square')
else:
    print('Not a perfect square')