# Check if a number is an Armstrong number

num = input("Enter num: ")
power = len(num)
if sum(int(digit)** power for digit in num) == int(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
