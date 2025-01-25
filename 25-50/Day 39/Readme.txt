Day 39&40 Flight Deals Tracking System : 

Overview
This project is a comprehensive flight deals tracking system that utilizes APIs for fetching flight details, managing data, and sending notifications. It automates the process of checking for the cheapest flights and notifies subscribed users of new deals.

Features
Flight Data Management:
The project uses a Google Sheet to store cities and track flight prices.
It leverages the Sheety API to manage the Google Sheet, including retrieving and updating city data, IATA codes, and flight prices.

IATA Code Lookup:
Missing IATA codes for cities are identified using the Amadeus API. The codes are then updated in the Google Sheet to ensure accurate flight searches.

Flight Search:
Flights are searched using the Amadeus API, focusing on round-trip, non-stop flights.
The search is conducted for a date range starting from the next day and extending up to six months.
The system retrieves details such as flight price, departure and arrival airports, and timings.

Notification System:
Users who subscribe via a Google Form are notified via email when a flight deal is found.
Emails include personalized messages with details about the flight, including price, departure, and arrival information.

Automation:
Data management, flight searches, and notifications are automated, ensuring seamless operation with minimal manual intervention.

Key Components
Data Manager:
Retrieves city data and flight prices from the Google Sheet.
Updates missing IATA codes and flight prices.

Flight Search:
Authenticates with the Amadeus API.
Fetches IATA codes for cities and searches for flights.
Finds the cheapest available flights for a given city.

Flight Data:
Orchestrates the interaction between the data manager and flight search modules.
Ensures that IATA codes and flight data are correctly updated.

Notification Manager:
Sends email notifications to users when a new flight deal is available.

Users Data:
Manages user subscription data from the Google Sheet.
Sends personalized emails to subscribed users about flight deals.

Learning Outcomes
API Integration:
Learned to interact with multiple APIs (Amadeus and Sheety) for data retrieval, processing, and updates.
Gained experience with authentication and secure API usage.

Data Management:
Implemented dynamic updates of missing IATA codes and flight prices in a Google Sheet using Python.