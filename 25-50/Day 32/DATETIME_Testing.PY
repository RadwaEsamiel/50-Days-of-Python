import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
print(now)
print(year)
print(month)


date_of_birth = dt.datetime(year= 1998, month= 4, day=1 )
print(date_of_birth)

dataofbirth = '1998-04-01'
dob = dt.datetime.strptime(dataofbirth, '%Y-%m-%d')
print(dob.year)