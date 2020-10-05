from datetime import datetime, date, timedelta
from dateutil import relativedelta

# Function to count days (returns int)
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.strptime(d2, "%d-%m-%Y")
    return abs((d2 - d1).days)

# Function that finds first day of week of given day and gets weeks diff between the two dates
def weeks_between(d1, d2):
    d1 = datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.strptime(d2, "%d-%m-%Y")
    monday1 = (d1 - timedelta(days=d1.weekday()))
    monday2 = (d2 - timedelta(days=d2.weekday()))
    return int(abs((monday2 - monday1).days)/7)

# Calculates months between two dates
def months_between(d1, d2):
    d1 = datetime.strptime(d1, "%d-%m-%Y")
    d2 = datetime.strptime(d2, "%d-%m-%Y")
    r = relativedelta.relativedelta(d2, d1)
    return abs(r.years * 12 + r.months)