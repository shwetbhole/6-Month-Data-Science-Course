# Determine how many days a month has

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
days = [31, 28 + (1 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 0), 31,
30, 31, 30, 31, 31, 30, 31, 30, 31]

print("Days:", days[month - 1])