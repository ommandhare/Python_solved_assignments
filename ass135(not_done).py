"""
Get two dates from config file and generate a report that shows
last Saturday of every month between these days

"""

from datetime import(
    datetime as DateTime,
    date as Date,
    time as Time,
    timedelta as TimeDelta
)
import csv
beginDate=Date(2024,1,1)

numdays=TimeDelta(days=30)

endDate=beginDate+numdays

print("beginDate : ",beginDate)
print("EndDate : ",endDate)



currentDate=beginDate
cnt=0
last_saturday=[]
while currentDate <= endDate:
    weekday=currentDate.weekday()
    if weekday==5:
           print(currentDate,currentDate.strftime("%A"))
           last_saturday.append((currentDate, currentDate.strftime('%A')))
           cnt+=1
    currentDate += TimeDelta(days=30)

    currentDate=tim(day=1)






print(cnt)
print(last_saturday)



# path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Date_time\first_mondays.csv"
#
# def write_to_csv(mondays):
#     with open(path, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['first_mondays'])
#         for date, weekday in mondays:
#             writer.writerow([date.strftime('%Y-%m-%d'), weekday])
#
# write_to_csv(mondays)
