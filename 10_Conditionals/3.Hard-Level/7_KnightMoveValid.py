# Check if a knight move in chess is valid

x1, y1 = map(int, input("Enter current position(x y)").split())
x2, y2 = map(int, input("Enter next position(x y)").split())

if (abs(x1 -x2), abs(y1 - y2) in [(2, 1), (1, 2)]):
    print("Valid Knight Move")
else:
    print("Invalid knight move")