# How do you handle incorrect inputs when you expect an integer using `input()`?

# try:
#     num = int(input('Enter a number: '))
# except ValueError:
#     print('Invalid input! Please enter a valid number.')

while True:
    try:
        num = int(input("Enter a number: "))
        break  # exit loop if valid
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# while True:
#     try:
#         num = float(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Invalid input! Please enter a valid number.")

# num_str = input("Enter a number: ")
# if num_str.isdigit():
#     num = int(num_str)
#     print("Valid number:", num)
# else:
#     print("Invalid input! Please enter only digits.")
