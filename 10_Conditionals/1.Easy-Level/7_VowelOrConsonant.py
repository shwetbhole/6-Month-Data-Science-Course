# Check if a character is a vowel or consonant

# 1ST METHOD:
character = input("Enter a character: ")

if character in "aeiou" or character in "AEIOU":
    print(f"{character} is a vowel")
else:
    print(f"{character} is consonant")

# 2ND METHOD (nit-method):

char = input("Enter a character: ").lower()

if char in "aeiou":
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")