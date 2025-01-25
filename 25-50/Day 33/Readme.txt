Day 33 : ISS Tracker and Notification System:

This project is an ISS Tracker and Notification System, designed to notify the user via email when the International Space Station (ISS) is overhead and it's dark outside at their location so they can see it. The application combines real-time data from APIs with email alerts, providing a practical and interesting project centered around space observation.

Key Features:

ISS Position Tracking:
The application uses the Open Notify API to fetch the current position of the ISS in real time. It then checks if the ISS is within a 5-degree radius of the user's latitude and longitude.

Daylight Checking:
The Sunrise-Sunset API is used to determine whether it is currently dark at the user's location. The application compares the current time with the sunrise and sunset times to ensure the ISS is only visible when it's dark.

Automated Email Notifications:
When the ISS is overhead and it's dark, the application sends an email to notify the user to look up and spot the ISS. It uses SMTP for email sending, and the email content is personalized to provide real-time alerts.

Efficient Use of Time Intervals:
The program checks the ISS position and daylight status every 60 seconds using the time.sleep() function, ensuring that the system remains efficient and avoids unnecessary API calls.

API Interaction: This project deepened my understanding of how to retrieve and manipulate data from web APIs using the requests library. I learned how to handle response data, such as JSON objects, and how to pass parameters effectively.

Geospatial Calculations: how to compare geographical coordinates to determine proximity, using latitude and longitude values to calculate if the ISS is overhead.

