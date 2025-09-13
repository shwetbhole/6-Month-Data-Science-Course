# Check if three numbers form a pythagorean triplet

a, b, c = sorted(map(int, input("Enter three numbers: ").split()))
if a**2 + b**2 == c**2:
    print("Pythagorean triplet")
else:
    print("Not a Pythagorean triplet")
