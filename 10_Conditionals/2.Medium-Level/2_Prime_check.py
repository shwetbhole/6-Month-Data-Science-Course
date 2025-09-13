# Determine if a number is a prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Not  a Prime number")
            break
        else:
            print("Prime number")
else:
    print("Not a prime number")