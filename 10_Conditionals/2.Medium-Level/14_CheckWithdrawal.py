# Check if a bank account balance is sufficient for withdrawal

balance = 100000
withdrawal = int(input("Enter withdrawal: "))
if balance >= withdrawal:
    print("Withdrawal Successful")
    print("Balance: ", balance-withdrawal)

else:
    print("Withdrawal Failed")
    print("Balance: ", balance)