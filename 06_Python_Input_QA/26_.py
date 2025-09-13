# Write a program that accepts a string and counts the occurrence of a particular character

text = input('Enter a string: ')
char = input('Enter a character to count: ')

print(f"Occurrence of {char}:{text.count(char)}")