import requests
import datetime
import os
from twilio.rest import Client

# Constants for Stock and Company
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Load sensitive data from environment variables
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")


# Function to get stock data
def get_stock_data(stock_symbol):
    url = 'https://www.alphavantage.co/query'
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "apikey": ALPHA_VANTAGE_API_KEY,
        "symbol": stock_symbol
    }
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["Time Series (Daily)"]


# Function to get latest news
def get_news(company_name):
    url_news = "https://newsapi.org/v2/everything"
    parameters_news = {
        "apiKey": NEWS_API_KEY,
        "q": company_name,
        "sortBy": "publishedAt",
        "language": "en"
    }
    response = requests.get(url_news, params=parameters_news)
    response.raise_for_status()
    news_data = response.json()
    first_three_articles = news_data['articles'][:3]
    return first_three_articles


# Calculate stock price difference and determine up/down
def calculate_stock_difference(daily_data):
    date_today = datetime.date.today()
    yesterday = str(date_today - datetime.timedelta(days=1))
    day_before = str(date_today - datetime.timedelta(days=2))

    try:
        yesterday_close = float(daily_data[yesterday]['4. close'])
        day_before_close = float(daily_data[day_before]['4. close'])
    except KeyError:
        raise KeyError("Data for the required dates is missing.")

    diff = yesterday_close - day_before_close
    up_down = "Up" if diff > 0 else "Down"
    percentage_change = round((abs(diff) / yesterday_close) * 100, 2)

    return up_down, percentage_change


# Function to send SMS via Twilio
def send_sms(up_down, percentage, articles):
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in articles:
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=f"{STOCK} is {up_down} by {percentage}%\nHeadline: {article['title']}\nBrief: {article['description']}",
            to=TO_PHONE_NUMBER
        )
        print(f"Sent message with SID: {message.sid}")


# Main script execution
if __name__ == "__main__":
    # Get stock and news data
    try:
        daily_data = get_stock_data(STOCK)
        news_articles = get_news(COMPANY_NAME)
    except requests.HTTPError as e:
        print(f"Failed to fetch data: {e}")
        exit(1)

    # Calculate percentage change
    up_down, percentage = calculate_stock_difference(daily_data)

    # Send SMS if change exceeds threshold
    if percentage > 5:
        send_sms(up_down, percentage, news_articles)
    else:
        print("No significant change detected.")
