import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NotificationManager:
    def __init__(self):
        self.sender_email = "radwaahmed55@yahoo.com"
        self.password = "yhrxdnyjimarnvzr"

    def send_email(self,receiver_email, mailbody):

        subject = "New Flight Deal Alert"

        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(mailbody, "plain"))

        try:

            with smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, msg.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
