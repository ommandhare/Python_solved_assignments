"""
Get two dates from config file and generate a report that shows 1st Monday of every months between these days

"""
from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
import csv

endDate=Date(2024,3,1)

numdays=TimeDelta(days=365)

beginDate=endDate-numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)



currentDate=beginDate
cnt=0
mondays=[]
while currentDate <= endDate:
    if currentDate.weekday()==0:
       print(currentDate,currentDate.strftime("%A"))
       mondays.append((currentDate, currentDate.strftime('%A')))
       cnt+=1
    currentDate += TimeDelta(days=5)
    # currentDate=tim(day=1)

print(cnt)
print(mondays)



path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\first_mondays.csv"

def write_to_csv(mondays):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['first_mondays'])
        for date, weekday in mondays:
            writer.writerow([date.strftime('%Y-%m-%d'), weekday])

write_to_csv(mondays)
