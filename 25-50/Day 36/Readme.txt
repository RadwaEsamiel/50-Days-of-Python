Day 36 : Stock Alert with News Notification: 

This project is a Stock Alert System that monitors the stock price of a specific company (in this case, Tesla Inc) and sends an SMS notification if the stock price experiences a significant change (more than 5%) from the previous day. The notification includes the percentage change and the latest news headlines related to the company.

Project Overview:

Stock Data Retrieval:
The system uses the Alpha Vantage API to fetch daily stock data for Tesla Inc (or any specified stock symbol).
It calculates the percentage change in the stock price compared to the previous day's closing price.

News Retrieval:
The News API is used to gather the latest news articles related to Tesla Inc. The system fetches the top 3 most recent articles.

SMS Notification:
When a significant change (greater than 5%) is detected in the stock price, an SMS notification is sent via Twilio API. The message contains:
The percentage change in stock price (up or down).
The headline and brief description of the latest news articles.