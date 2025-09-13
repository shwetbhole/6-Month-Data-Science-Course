# Implement a ticket pricing system

age = int(input("Enter age: "))

if age < 5:
    print("Ticket Price: Free")
elif age >= 60:
    print("Ticket Price: $50")
else:
    print("Ticket Price: $100")