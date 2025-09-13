# Check if number is a single-digit number

num = int(input("Enter a number: "))

if abs(num) < 10:   # absolute makes the negative to positive
    print("Single-digit number")
else:
    print("Not a single-digit number")