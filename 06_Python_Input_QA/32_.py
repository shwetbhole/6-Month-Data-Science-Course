# Write a program that checks if the entered number is divisible by both 3 and 5.

num = int(input('Enter the number: '))

if num%3==0 and num%5==0:
    print('Divisible by both 3 and 5')
else:
    print('Not divisible by both 3 and 5')

