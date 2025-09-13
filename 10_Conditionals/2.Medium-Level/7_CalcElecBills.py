# Calculate electricity bill

unit = int(input("Enter electricity units consumed: "))

if unit<=100:
    bill = unit*5
elif unit<=300:
    bill = (100*5) + (unit-100) * 100
else:
    bill = (100*5) + (200*10) + (unit - 300) * 15
print("Total Bill: $", bill)