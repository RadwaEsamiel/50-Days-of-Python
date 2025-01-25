Day 32 : Birthday Reminder Application 
This project is a Birthday Reminder Application that allows users to store, manage, and send birthday wishes via email. The application combines data handling and email functionality to create a personalized greeting experience for friends and family.

Key Features:

Data Storage:
Users can input names, email addresses, and birthdays, which are stored in a CSV file. This feature allows easy management of birthday information.

Birthday Checking:
The application checks the current date against the stored birthdays. If it finds any matches, it collects the names and email addresses of those whose birthdays fall on that day.

Personalized Letters:
The application randomly selects a birthday letter template from a predefined set. Each letter template includes a placeholder for the recipient's name, which is dynamically replaced with the actual name of the person whose birthday it is.

Email Sending:
Using the Simple Mail Transfer Protocol (SMTP), the application sends personalized birthday greetings to the corresponding email addresses. This functionality ensures that users can wish their loved ones directly through the application.


Date and Time Manipulation: The project allowed me to work with the datetime module to handle and compare dates, ensuring that birthday notifications are accurate and timely.

Email Communication via SMTP: experience in using the smtplib library to send emails programmatically, learning how to manage email authentication and handle potential errors in the process.
