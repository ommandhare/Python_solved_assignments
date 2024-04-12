"""
Get date from config file and display date and date-365 days (same thing you can do using 1 year or 12 months)

"""

from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)


mydate=Date(2021,6,26)

print(mydate)
print("############")
print(mydate+TimeDelta(days=365))
