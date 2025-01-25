import datetime as dt
import random as rm
import smtplib

current_date = dt.datetime.now()
today = current_date.weekday()

with open("quotes.txt") as data :
    quotes = data.readlines()

random_quote = rm.choice(quotes)
print(random_quote)

my_email = "pyprojectbirthday@gmail.com"
my_password = "00795093"

if today == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="radwaahmed55@yahoo.com",
                            msg="Subject:hello\n\n"
                                f"{random_quote}")

