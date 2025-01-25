import requests
from twilio.rest import Client
import os

api_key = os.environ.get("WEATHER_API_KEY")
weather_data = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.environ.get("S_ID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 31.200092,
    "lon": 29.918739,
    "appid" : api_key,
    "cnt" : 4

}
will_rain = False

response = requests.get(weather_data, params=parameters)
response.raise_for_status()
data = response.json()
for hour in data['list'] :
    if hour['weather'][0]['id'] < 700 :
        will_rain = True

if will_rain :
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_= "+18135345692",
    body = "It's going to rain. bring and umbrella",
    to = "+18777804236")
    print(message.status)

