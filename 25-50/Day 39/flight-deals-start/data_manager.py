import requests

# google form : https://forms.gle/oycvZFWtHBb5D6hj6
# google sheet : https://docs.google.com/spreadsheets/d/1Hod21F6aRlS18EP4xPFXmcAmrSmAMu2S1YLmpRKDK-8/edit?resourcekey=&gid=0#gid=0

class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = "https://api.sheety.co/3ca87c78d6f304317c0166e2620325e8/flightClubDeals/prices"
        self.response = requests.get(self.SHEETY_ENDPOINT)
        self.response.raise_for_status()
        self.data = self.response.json()


    def cities_data(self):
        cities = {}
        for row in self.data['prices']:
            if not row.get('iataCode'):
                cities[row['id']] = row['city']

        return cities

    def update_cities(self,row, iata_code):
            sheety_data = {
                "price": {
                    "iataCode": iata_code
                }
            }

            update_response = requests.put(f"{self.SHEETY_ENDPOINT}/{row}", json=sheety_data)
            update_response.raise_for_status()

    def flights_data_dict(self):
        flight_data_dict = {}
        for row in self.data['prices']:
            iata_code = row.get('iataCode')
            lowest_price = row.get('lowestPrice')

            flight_data_dict[row['id']] = [iata_code, lowest_price]

            if not iata_code:
                print(f"Missing 'iataCode' for row with ID {row['id']}: {row}")

        return flight_data_dict

    def update_prices(self,row, price):
            sheety_data = {
                "price": {
                    "lowestPrice": price
                }
            }

            update_response = requests.put(f"{self.SHEETY_ENDPOINT}/{row}", json=sheety_data)
            update_response.raise_for_status()








