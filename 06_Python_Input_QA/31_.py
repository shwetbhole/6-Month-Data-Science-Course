# How would you accept a date input from the user in Python?

from datetime import datetime

date_str = input('Enter a data(YYYY-MM-DD): ')

date = datetime.strptime(date_str, "%Y-%m-%d")

print('Entered Date: ',date)
