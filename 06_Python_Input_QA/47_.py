# Write a program to find the average of a list of numbers entered by the user.

numbers = list(map(int, input('Enter numbers separated by spaces: ').split()))

print(f"Average: {(sum(numbers)/len(numbers)):.4f}")