import requests
import notification_manager
# google form : https://forms.gle/oycvZFWtHBb5D6hj6

class UsersEmails:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/3ca87c78d6f304317c0166e2620325e8/flightClubDeals/usersInfo"
        self.response = requests.get(self.SHEETY_ENDPOINT)
        self.response.raise_for_status()
        self.data = self.response.json()


    def email_users(self, infolist):
        for row in self.data['usersInfo']:
            first_name = row['whatIsYourFirstName ?']
            email = row['whatIsYourEmail?']
            mailbody = (f"Hello {first_name}"
                        f"A new flight Deal is available you can get a ticket that departs from {infolist[1]} "
                        f" at {infolist[2]} and arrives to {infolist[3]} at {infolist[4]} only four {infolist[0]}"
                        f"check out the website for more details!")
            sendemail = notification_manager.NotificationManager()
            send_email = sendemail.send_email(email, mailbody)


