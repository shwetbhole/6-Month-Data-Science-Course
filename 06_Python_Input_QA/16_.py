# Write a program that checks if the input number is a prime number.

num = int(input('Enter a number: '))


if num>1:
    for i in range(2, num):
        if num%i ==0:
            print('Not Prime')
            break

        else:
            print('Prime')
else:
    print('Not prime')