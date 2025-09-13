# Implement a loan eligibility checker

income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
employed = input("Are you employed? (yes/no): ").lower()

if income >= 25000 and credit_score >= 700 and employed == "yes":
    print("Loan Approved")
else:
    print("Loan Denied")