import requests
import json
import datetime as dt
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
data_file = data["iss_position"]
print(data_file)

lat = 31.200092
lng = 29.918739

parameter = {
"lat" : lat,
"lng" : lng,
"formatted" : 0
}
res = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
data = res.json()

sunrise =data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)

today_now = dt.datetime.now().hour
print(today_now)