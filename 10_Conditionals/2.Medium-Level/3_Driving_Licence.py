# Check if a person is eligible for a driving license

age = int(input("Enter Age: "))
passed_test = input("Did you pass the test? (y/n): ").lower()

if age>=18 and passed_test=='y':
    print("Eligible for a driving licence")
else:
    print("Not eligible")