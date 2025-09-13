# Determine the type of quadrilateral

print("a->b->c->d->a")
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
d = int(input("Enter fourth side: "))

if a==b==c==d:
    print("square")
elif a==c or b==d:
    print("Rectangle")
else:
    print("Other Quadrilateral")