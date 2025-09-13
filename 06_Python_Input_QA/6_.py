# How do you convert user input to a list of integers?

# After using 'split()', you can convert each element to an integer using a list comprehension

num = [int(x) for x in input("Enter numbers: ").split()]

print(num)

print(type(num))
