# How do you find the maximum number from a list of integers entered by the user?

numbers = list(map(int, input('Enter numbers separated by spaces: ').split()))

print('Maximum number: ', max(numbers))