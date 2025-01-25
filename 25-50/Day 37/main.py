from datetime import datetime
from multiprocessing.managers import Token

import requests


TOKEN = "hellothisradwaahmedesmaiel"
USERNAME = "radwa"
endpoint = "https://pixe.la/v1/users"

user_parameters = {"token": Token,
                   "username": USERNAME,
                   "agreeTermsOfService":"yes",
                   "notMinor":"yes"}

# response = requests.post(url=endpoint,json=user_parameters)
# print(response.text)

graph_endpoint = f"{endpoint}/{USERNAME}/graphs"


graph_parameters = {"id":"graph1",
                    "name":"Coding Graph",
                    "unit":"Hour",
                    "type":"int",
                    "color":"sora"}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=graph_endpoint,json=graph_parameters, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/radwa/graphs/graph1.html

pixel_endpoint = f"{endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()

data_parameters = {"date": today.strftime("%Y%m%d"),
                   "quantity":"3"}

# response = requests.post(url=pixel_endpoint,json=data_parameters, headers=headers)
# print(response.text)


update_endpoint = f"{endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
updated_parameters = {"quantity":"5"}

# response = requests.put(url=update_endpoint,json=updated_parameters, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)


