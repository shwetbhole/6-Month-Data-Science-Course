# Write a program to swap the values of two variables using `input()`.

a = input('Enter first value: ')
b = input('Enter second value: ')

a, b = b, a

print(f"Swapped values: a = {a}, b = {b}")