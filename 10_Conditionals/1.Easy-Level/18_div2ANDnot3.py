# Check if a number is divisible by 2 but not by 3

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 != 0:
    print("Divisible by 2 but not by 3")
else:
    print("Does not meet criteria")