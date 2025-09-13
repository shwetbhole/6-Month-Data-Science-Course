# Write a program that accepts a sentence and prints the longest word

text = input('Enter a string: ')
words = text.split()
longest_word = max(words, key = len)
print('longest word:', longest_word)