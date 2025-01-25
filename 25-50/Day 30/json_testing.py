import json

# with open("passwords_dict.json", "r") as pass_data:
#     data = json.load(pass_data)
#     print(data)

website = "google"
try :
    with open("passwords.json") as passwords_data :
        passwords = json.load(passwords_data)
        data = passwords[website]
        print(data)
except :
    print("no data found")