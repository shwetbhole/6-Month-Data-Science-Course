# Print "Good Morning" if the time is before 12 PM, otherwise print "Good Afternoon"

hour = int(input("Enter Hour (24-hour format): "))

if hour <= 12:
    print("Good morning")
else:
    print("Good afternoon")