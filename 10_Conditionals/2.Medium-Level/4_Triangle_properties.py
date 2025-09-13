# Determine if a triangle is equilateral, isosceles, or scalene

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a==b or a==c or b==c:
    print("Isosceles Triangle")
else:
    print("Scalar Triangle")