import requests
import time
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self):
        self.Flight_api_key = "MnzCoEwNR2sa5nQnwNj1PyqufFvkzauc"
        self.Flight_api_secret = "bEbA1Dz2tqJcgR3S"
        self.Flight_auth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.locations_url = "https://test.api.amadeus.com/v1/reference-data/locations"
        self.search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.Flight_auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.Flight_api_key,
            "client_secret": self.Flight_api_secret
        }
        self.token_expiry_time = None
        self.access_token = None
        self.flights = []

    def requesting_auth(self):
        if self.access_token and datetime.now() < self.token_expiry_time:
            return self.access_token

        auth_response = requests.post(self.Flight_auth_url, data=self.Flight_auth_data)
        auth_response.raise_for_status()
        self.access_token = auth_response.json().get("access_token")
        expires_in = auth_response.json().get("expires_in")
        self.token_expiry_time = datetime.now() + timedelta(seconds=expires_in)
        return self.access_token

    def requesting_data(self, cities):
        access_token = self.requesting_auth()
        headers = {"Authorization": f"Bearer {access_token}"}
        dict_cities = {}

        for city_id, city_name in cities.items():
            city_name = city_name.strip().lower().title()
            params = {"keyword": city_name, "subType": "CITY"}
            city_iata_response = requests.get(self.locations_url, headers=headers, params=params)
            city_iata_response.raise_for_status()
            city_iata_codes = city_iata_response.json()

            if city_iata_codes.get("data"):
                iata_code = city_iata_codes['data'][0]['iataCode']
                dict_cities[city_id] = [city_name, iata_code]
            else:
                dict_cities[city_id] = [city_name, None]

            time.sleep(1)
        return dict_cities


    def get_cheapest_flight(self, origin, destination,departure_date,return_date):
        access_token = self.requesting_auth()
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        # Parameters to find a round-trip, non-stop flight with GBP price
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "currencyCode": "GBP",  # Ensure price is returned in GBP
            "nonStop": "true",  # Ensure non-stop flight
            "max": 10,  # Get the cheapest flight
        }

        response = requests.get(self.search_endpoint, headers=headers, params=params)
        response.raise_for_status()

        flights_data = response.json()

        if "data" in flights_data and flights_data["data"]:
            price = flights_data["data"][0]["price"]["total"]
            departure_airport = flights_data["data"][0]["segments"][0]["departure"]["iataCode"]
            departure_time = flights_data["data"][0]["segments"][0]["departure"]["at"]
            arrival_airport = flights_data["data"][0]["segments"][0]["arrival"]["iataCode"]
            arrival_time = flights_data["data"][0]["segments"][0]["arrival"]["at"]
            self.flights.append([price, departure_airport, departure_time, arrival_airport, arrival_time])
        else:
            print(f"No flights found for route {origin} to {destination}.")

        return self.flights
