# Check if a number is a Harshad number/Niven number
from unicodedata import digit

num = int(input("Enter a number: "))
sum_digits = sum(int(digit) for digit in str(num))

if num % sum_digits == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")