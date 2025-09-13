# Print "Weekend" if the day is Saturday or Sunday; otherwise, print "Weekday"

day = input("Enter a day: ").lower()

if day in ["saturday", "sunday"]:
    print('week-end')
else:
    print('week-day')