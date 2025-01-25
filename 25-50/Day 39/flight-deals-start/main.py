import data_manager
import flight_search
import flight_data
import time
from datetime import datetime, timedelta
import users_data

ORIGIN = "CIR"

flight_data_structure = flight_data.FlightData()
flight_search = flight_search.FlightSearch()
flight_data_structure.data_structure()


flights_data_manager = data_manager.DataManager()
data_dict = flights_data_manager.flights_data_dict()

# Set the departure and return date range
departure_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
return_date = (datetime.now() + timedelta(days=180)).strftime('%Y-%m-%d')

notifications = users_data.UsersEmails()

for data in data_dict.items():
    row = data[0]
    city = data[1][0]
    price = data[1][1]

    # Skip if city or IATA code is invalid
    if not city:
        print(f"Invalid IATA code for row {row}. Skipping.")
        continue

    time.sleep(60)
    lowest_price_list = flight_search.get_cheapest_flight(ORIGIN, city, departure_date, return_date)

    if not lowest_price_list:
        print(f"No flights found for {city}.")
        continue


    lowest_price = float(lowest_price_list[0][0])  # Ensure type safety
    if price is None or lowest_price < price:
        flights_data_manager.update_prices(row, lowest_price)
        print(f"Price updated for {city}.")
        notifications.email_users(lowest_price_list)









