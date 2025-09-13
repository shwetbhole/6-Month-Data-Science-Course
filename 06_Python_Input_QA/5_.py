# How do you check if a number entered by the user is positive,
# negative, or zero?

# Use an 'if-elif-else' block to check the condition:

num = int(input('Enter a number: '))

if num>0:
    print('Positive')
elif num<0:
    print('Negative')
else:
    print('Zero')