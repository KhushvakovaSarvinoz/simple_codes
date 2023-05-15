import datetime as dt
now= dt.datetime.now()
print(now)

today=dt.date.today()
birth_day=dt.date(2023,10,6)
left=birth_day-today
print(left)