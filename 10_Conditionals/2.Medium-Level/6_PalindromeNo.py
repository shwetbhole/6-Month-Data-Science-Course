# Check if a number is a palindrome

num = input("Enter number: ")

if num == num[::-1]:
    print("Palindrome")
else:
    print('Not Palindrome')