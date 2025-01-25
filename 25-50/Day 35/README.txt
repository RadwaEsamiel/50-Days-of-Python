Day 35 : Weather Alert Notification :
This project is a Weather Alert Notification System that uses the OpenWeatherMap API to forecast upcoming weather and sends an SMS alert via Twilio if rain is expected. The application demonstrates the integration of a weather data API with SMS notification services, providing real-time updates to help users prepare for rain.

Project Overview

API Integration for Weather Data:
The app pulls weather data using the OpenWeatherMap API. Forecast data for the specified location is requested and processed to check for rain conditions in the upcoming hours.

Automated Notification via Twilio:
When rain is detected in the forecast, the app uses Twilio’s API to send an SMS alert. This alert serves as a proactive reminder to carry an umbrella. The Twilio credentials and weather API key are securely accessed from environment variables to protect sensitive information.

Configuration and Parameters:
Location parameters (latitude and longitude) are customizable, allowing flexibility to monitor weather for different locations.
Forecast count is set to analyze the next few hours, keeping alerts relevant and timely.


Environment Variable Management: Sensitive data such as API keys and authorization tokens are managed via environment variables, which enhances security and prevents hardcoding sensitive information.
