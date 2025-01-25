import pandas as pd
import datetime as dt
import smtplib
import random

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")
today = dt.datetime.now()

# 2. Check if today matches a birthday in the birthdays.csv
today_birthdays = birthdays[(birthdays.month == today.month) & (birthdays.day == today.day)]

if today_birthdays.empty:
    print("No birthdays today")
else:
    today_birthdays_names_emails = today_birthdays[['name', 'email']].values.tolist()

    # 3. If step 2 is true, pick a random letter from letter templates and replace [NAME]
    with open(r"letter_templates\letter_1.txt") as letter_1:
        letter_1 = letter_1.read()

    with open(r"letter_templates\letter_2.txt") as letter_2:
        letter_2 = letter_2.read()

    with open(r"letter_templates\letter_3.txt") as letter_3:
        letter_3 = letter_3.read()

    letters = [letter_1, letter_2, letter_3]

    my_email = "radwaahmed55@yahoo.com"
    my_password = "yhrxdnyjimarnvzr"

    # 4. Send the letter to each birthday person
    for name_email in today_birthdays_names_emails:
        random_letter = random.choice(letters)
        letter = random_letter.replace('[NAME]', name_email[0])

        try:
            with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
                connection.login(user=my_email, password=my_password)
                msg = f"""\
From: {my_email}
To: {name_email[1]}
Subject: Happy Birthday!!

{letter}
"""
                connection.sendmail(from_addr=my_email,
                                    to_addrs=name_email[1],
                                    msg=msg)
            print(f"Sent email to {name_email[0]} at {name_email[1]}")
        except Exception as e:
            print(f"Failed to send email to {name_email[0]} ({name_email[1]}): {e}")
            print(letter)
