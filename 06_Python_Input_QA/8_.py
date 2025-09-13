# Write a Python program that accepts a string and prints the
# number of vowels in it.

text = input("Enter a string: ")

vowels = "aeiou"

count = sum(1 for char in text if char.lower() in vowels)

print("Number of vowels: ", count)
