import time

import requests
import json
import datetime as dt
import smtplib


MY_Latitude = 31.200092
MY_Longitude = 29.918739

def iss_position(lat,lng):
    ISS_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    ISS_response.raise_for_status()

    ISS_data = ISS_response.json()
    ISS_Latitude = float(ISS_data["iss_position"]["latitude"])
    ISS_Longitude = float(ISS_data["iss_position"]["longitude"])

    close = False
    if lat + 5 >= ISS_Latitude >= lat - 5 :
        close = True
    if lng + 5 >= ISS_Longitude >= lng - 5 :
        close = True
    return close


def is_dark(lat,lng) :
    dark = False

    parameter = {
        "lat": lat,
        "lng": lng,
        "formatted": 0
    }
    SUN_response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    SUN_data = SUN_response.json()

    sunrise = int(SUN_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(SUN_data['results']['sunset'].split("T")[1].split(":")[0])

    current_hour = dt.datetime.now().hour

    if current_hour <= sunrise or current_hour >= sunset :
        dark = True

    return dark


while True :
    time.sleep(60)
    if iss_position(MY_Latitude,MY_Longitude) and  is_dark(MY_Latitude,MY_Longitude) :

        my_email = "radwaahmed55@yahoo.com"
        my_password = "jleddhxjgrzdokri"

        try:
            with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as connection:
                connection.login(user=my_email, password=my_password)

                msg = f"""\
                From: {my_email}
                To: "radwaesmaiel13@gmail.com"
                Subject: LOOKUP!!
                
                ISS is Above You! Look up to see it!
    """
                connection.sendmail(from_addr=my_email,to_addrs="radwaesmaiel13@gmail.com",msg=msg)
                print(f"Sent email to Radwa!")

        except Exception as e:
                print(f"Failed to send email to Radwa): {e}")

