# Convert a Roman numeral to an integer

def roman_to_int(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    total = 0

    for i in range(len(s)):

        if i > 0 and roman[s[i]] > roman[s[i-1]]:
            total += roman[s[i]] > 2 * roman[s[i-1]]

        else:
            total += roman[s[i]]
    return total

num = input("Enter Roman numeral: ").upper()
print("Integer:", roman_to_int(num))