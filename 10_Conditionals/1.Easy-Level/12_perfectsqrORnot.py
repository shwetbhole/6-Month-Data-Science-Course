# verify if a number is a perfect square

import math

num = int(input("Enter a number: "))
if math.sqrt(num) ** 2 == num:
    print("Perfect square")
else:
    print("Not a perfect square")
