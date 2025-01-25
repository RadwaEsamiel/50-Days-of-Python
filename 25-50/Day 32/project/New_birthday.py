
import pandas as pd
import datetime as dt


birthday_name = input("Enter name : ").title()
birthday_email = input("Enter Email : ")
birthday_date = input("Enter Date in format 'Year-month-day': ")

dob = dt.datetime.strptime(birthday_date,'%Y-%m-%d')

birthdays = pd.read_csv("birthdays.csv")

new_birthday = {"name" : birthday_name,
               "email" : birthday_email,
                "year": dob.year,
                "month" : dob.month,
                "day" : dob.day}

new_birthday_df = pd.DataFrame([new_birthday])

birthdays = pd.concat([birthdays,new_birthday_df], ignore_index=True)
print(birthdays)
birthdays.to_csv("birthdays.csv")