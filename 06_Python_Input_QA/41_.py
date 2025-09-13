# How would you prompt the user for input until they enter a valid number?

while True:
    try:
        num = int(input('Enter a valid number: '))
        break

    except ValueError:
        print('Invalid input. Please try again.')