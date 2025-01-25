import smtplib

my_email = "radwaahmed55@yahoo.com"
my_password = "xkekejbfjixthguw"

with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
    connection.login(user=my_email, password=my_password)
    msg = """\
From: radwaahmed55@yahoo.com
To: radwaesmaiel13@gmail.com
Subject: Hello

This is the email body.
"""
    connection.sendmail(from_addr=my_email,
                        to_addrs="radwaesmaiel13@gmail.com",
                        msg=msg)
