import requests
from datetime import datetime

APP_ID = "9c236f1a"
API_KEY = "a8a4cee1366bd3c21bab0c1112b91628"
AUTH_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMLheAAAAAAA0%2BuSeid%2BULvsea4JtiGRiSDSJSI%3DEUifiRBkKG5E2XzMDjRfl76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/ea6815c51f3d35a58c30defe9496baff/copyOfMyWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


exercise_and_duration = input("What kind on exercise did you do? and for what duration in Minutes?")


data = {
    "query": exercise_and_duration,
    "gender": "female",
    "weight_kg": 55,
    "height_cm": 160,
    "age": 26
}


response = requests.post(url, headers=headers, json=data)

exercise_data = response.json()

exercise = exercise_data['exercises'][0]['user_input'].title()
duration_min = exercise_data['exercises'][0]['duration_min']
calories = exercise_data['exercises'][0]['nf_calories']
current_datetime = datetime.now()
time = current_datetime.strftime("%H:%M:%S")
day = current_datetime.strftime("%d/%m/%Y")


row_data = {
    "workout": {
        "date": day,
        "time": time,
        "exercise": exercise,
        "duration": duration_min,
        "calories": calories

    }
}


add_row = requests.post(SHEETY_ENDPOINT, json=row_data, headers={"Authorization": f"Bearer {AUTH_TOKEN}"})

if add_row.status_code == 200:
    print("Data added successfully!", add_row.text)
else:
    print("Failed to add Data:", add_row.text)



