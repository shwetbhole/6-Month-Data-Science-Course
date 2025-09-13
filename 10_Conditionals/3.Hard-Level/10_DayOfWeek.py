# Find the day of the week for a given date (without built-in functions)

def day_of_week(d, m, y):
    if m<3:
        m+=12
        y-=1
    k =y%100
    j =y//100
    day = (d+(13*(m+1))//5+k+(k//4)+(j//4)-2*j)%7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday","Thursday", "Friday"]
    return days[day]

day, month, year = map(int, input("Enter date (DD MM YYYY)").split())
print("Day of the week:", day_of_week(day, month, year))
